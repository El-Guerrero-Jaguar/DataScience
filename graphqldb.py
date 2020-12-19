"""
This module helps connect to the GraphQL API to feed the database
"""

from python_graphql_client import GraphqlClient


GRAPHQL_URL = 'http://ec2-3-21-233-42.us-east-2.compute.amazonaws.com:3000/api'
client = GraphqlClient(endpoint = GRAPHQL_URL)


def send_graphql_data(data):
    """
    Sends the input data according to the mutation
    """
    mutation = """mutation MutationVacant(
                    $title:String!,
                    $company:String!,
                    $description:String!,
                    $town:String!,
                    $modality:String!,
                    $date:Date!,
                    $salary:String!,
                    $urlVacant:String!,
                    $urlCompany:String!
                ){
                    AddVacant(
                        title:$title,
                        company:$company,
                        description:$description,
                        town:$town,
                        modality:$modality,
                        date:$date,
                        salary:$salary,
                        urlVacant:$urlVacant,
                        urlCompany:$urlCompany
                    ){
                        title,
                        company,
                        description,
                        town,
                        modality,
                        date,
                        salary,
                        urlVacant,
                        urlCompany
                    }
                }
    """



    responses = []

    for item in data:
        #print(item['fecha'])
        fields = {
                    'title': item['titulo'],
                    'company': item['empresa'],
                    'description': item['descripcion'],
                    'town': item['pais'],
                    'modality': item['modalidad'],
                    'date': item['fecha'],
                    'salary': item['salario'],
                    'urlVacant': item['url_vacante'],
                    'urlCompany': item['url_empresa']
                }

        responses.append(client.execute(query = mutation, variables = fields))

    # return client.execute(query = mutation, variables = {
    #     "title":"titl prueba",
    #     "company":"company de prueba",
    #     "description":"description",
    #     "town":"town",
    #     "modality":"modality",
    #     "date":"2020-10-12",
    #     "salary":"salary",
    #     "urlVacant":"urlVacant",
    #     "urlCompany":"urlCompany"
    # })

    return responses