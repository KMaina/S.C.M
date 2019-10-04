create_product_mutation = '''
mutation{
  createProduct(name:"Egg", manufacturer:"none", price:200, tax:0, uom:"none"){
    product{
      name
    }
  }
}
'''

create_product_response = {"data": {"createProduct": {"product": {"name": "Egg"}}}} # noqa

edit_product_mutation = '''
mutation{
  updateProduct(id:1, name:"Dishy", manufacturer:"none",
                price:200, tax:0, uom:"none"){
    product{
      name
    }
  }
}
'''

edit_product_response = {"data": {"updateProduct": {"product": {"name": "Dishy"}}}} # noqa

delete_product_mutation = '''
mutation{
  deleteProduct(id:1){
    product{
      name
    }
  }
}
'''

delete_product_response = {"data": {"deleteProduct": {"product": {"name": "Eggs"}}}} # noqa
