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

    for i in range(len(data)):
        fields = {
                    'title': data[i]['titulo'],
                    'company': data[i]['empresa'],
                    'description': data[i]['descripcion'],
                    'town': '',
                    'modality': data[i]['modalidad'],
                    'date': data[i]['fecha'],
                    'salary': data[i]['salario'],
                    'urlVacant': data[i]['url_vacante'],
                    'urlCompany': data[i]['url_empresa']
                }

        responses.append(client.execute(query = mutation, variables = fields))

    return responses