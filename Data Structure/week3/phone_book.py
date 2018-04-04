# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    dic = {}
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            dic[cur_query.number] = cur_query.name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else: # otherwise, just add it
            #     contacts.append(cur_query)
        elif cur_query.type == 'del':
            try:
                del dic[cur_query.number]
            except:
                pass

        else:
            response = 'not found'
            try:
                response = dic[cur_query.number]
            except:
                pass
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

