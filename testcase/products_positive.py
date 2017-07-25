from tools import req
from tools import dbconnect
import json


rq = req.REQ()
qry = dbconnect.Dbconnect()

def Create_a_Product():
    """
    Function to make 'products' API call to create a product.
    Some value for payload are hardcoded, the call made and then the data in the response verified.
    """

    print "Running 'create product' endpoint test ...."

    # set global variables to be used in different functions
    global product_id
    global title
    global price

    # create payload for the call
    title = 'Test1 Title'
    price = '9.99'

    input_data = {
                        'product':{
                            'title':title,
                            'type':'simple',
                            'regular_price': price}}

    info = rq.post('products',input_data)
    #print info
    print info[0]
    print json.dumps(info[1],indent=4)


def verify_product_created_in_db():
    """
    Function to query the data base and verify product is created with the correct information.

    Note:
        This function depends on the first function 'test_create_a_product()' being called first. The variables
        set in that function are used in this function.
    """

    print "Querying the database to get product information"

    sql = '''SELECT p.post_title, p.post_type, pm.meta_value FROM wp_posts p JOIN wp_postmeta pm
            ON p.id=pm.post_id WHERE p.id={} AND pm.meta_key='_regular_price' '''.format(563)
#    sql = '''SELECT * From wp_users'''
    qrs = qry.select('infotechads', sql)

    # extracting the data
    product_title = qrs[0][0]
    product_type = qrs[0][1]
    product_price = qrs[0][2]
    print(qrs)

    title = "Test1 Title different"
    print "Verifying the product title"
    assert product_title == title, "The Tile in DB is not as Expected . Product title : {}, Expected : {}".format(product_title, title)

#Create_a_Product()
verify_product_created_in_db()
