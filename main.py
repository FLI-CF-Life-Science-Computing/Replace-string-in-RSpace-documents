# coding=utf-8
"""
Searches all documents of an RSpace ELN account for a character string in order to replace it and upload the edited document as a new version.
Your have to check the API limits (https://researchspace.helpdocs.io/article/oz02ygufnj-api-configuration-and-setup) because the script can create many api requests.
"""

# @status:  production
# @version: 1.0
# @author:  Fabian Monheim (fabian.monheim@leibniz-fli.de)
import sys
import rspace_client
import logging
import time
 


def print_document_names(response): # Function is not used but you can activate it to print all document names, ids,.. found searching for the ORIGINALTEXT
    print('Documents in response:')
    for document in response['documents']:
        print(document['name'], document['id'], document['lastModified'], document['globalId'])
        
try:
    API_KEY         = ""
    ELN_URL         = ""
    ORIGINALTEXT    = ''
    NEWTEXT         = ''
    
    logging.basicConfig(filename='main.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
    
    advanced_query = rspace_client.AdvancedQueryBuilder().\
    add_term(ORIGINALTEXT, rspace_client.AdvancedQueryBuilder.QueryType.FULL_TEXT).\
    get_advanced_query()

    client = rspace_client.Client(ELN_URL,API_KEY)
    response = client.get_documents_advanced_query(advanced_query)
    #print_document_names(response)
    for document in response['documents']:
        try:
            time.sleep(2) # Wait two second because of the standard minimum interval of 25ms between requests
            single_doc = client.get_document(document['id'])
            document_id = single_doc['id'] 
            logging.info('Found document {}'.format(document_id))
            dict_fields = single_doc['fields'][0]
            original_content = dict_fields["content"]
            if (original_content.find(ORIGINALTEXT)!=-1):   
                new_content = original_content.replace(ORIGINALTEXT,NEWTEXT)
                upload_data = [{'content': new_content}]
                response = client.update_document(document_id,None,None,None,upload_data)
                logging.info('Document {} updated'.format(document_id))
            else:
                logging.info('No matching string found in document {}'.format(document_id)) 
        except BaseException as e: 
            logging.warning('Error: {} in line {}'.format(e, sys.exc_info()[2].tb_lineno))    
           
except BaseException as e: 
    logging.warning('Error: {} in line {}'.format(e, sys.exc_info()[2].tb_lineno))
    sys.exit(0)  

