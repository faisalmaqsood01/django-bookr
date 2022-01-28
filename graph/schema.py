import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from apis.models import Product, CartItem


class ProductType(DjangoObjectType):
  class Meta:
    model = Product
    fields = ('id', 'name', "price", "quantity", 'description')


class CartItemType(DjangoObjectType):
  class Meta:
    model = CartItem
    fields = (
      'user',
      'product',
      'quantity',
    )


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
  products = graphene.List(ProductType)
  userBuyItems = graphene.List(CartItemType)

  def resolve_products(root, info, **kwargs):
    # Querying a product
    return Product.objects.all()

  def resolve_userBuyItems(root, info, **kwargs):
    # Querying a list
    # See if a user is authenticated
    if info.context.user.is_authenticated:
      return CartItem.objects.filter(user=info.context.user.id).select_related('user', 'product')
    else:
      return CartItem.objects.all().select_related('user', 'product')


"Mutations Code"


class ProductsInput(graphene.InputObjectType):
  name = graphene.String(description='Input product name')
  price = graphene.Int(description='Input product price')
  quantity = graphene.Int(description='Input quantity')
  description = graphene.String(description='Input description')


class createProductItem(graphene.Mutation):
  class Arguments:
    input = ProductsInput(required=True)

  productItem = graphene.Field(ProductType)

  @classmethod
  def mutate(cls, root, info, input):
    productItem = Product()
    productItem.name = input.name
    productItem.price = input.price
    productItem.quantity = input.quantity
    productItem.description = input.description
    productItem.save()
    return createProductItem(productItem=productItem)


class CartItemsInput(graphene.InputObjectType):
  user = graphene.Int(description='Input Valid User ID')
  product = graphene.Int(description='Input Valid product ID')
  quantity = graphene.Int(description='Input quantity')


class createCartItem(graphene.Mutation):
  class Arguments:
    input = CartItemsInput(required=True)

  cartItem = graphene.Field(CartItemType)

  @classmethod
  def mutate(cls, root, info, input):
    cartItem = CartItem()
    get_user = User.objects.get(id=input.user)
    get_product = Product.objects.get(id=input.product)
    cartItem.user = get_user
    cartItem.product = get_product
    cartItem.quantity = input.quantity
    cartItem.save()
    return createCartItem(cartItem=cartItem)


class Mutation(graphene.ObjectType):
  create_cart_item = createCartItem.Field()
  create_product_item = createProductItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
