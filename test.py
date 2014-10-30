import camomile.client


def empty_database(root_client):
	code, l_queue = root_client.get_all_queue()
	for ele in l_queue:
		root_client.delete_queue(ele["_id"])

	code, l_annotation = root_client.get_all_annotation()
	for ele in l_annotation:
		root_client.delete_annotation(ele["_id"])

	code, l_layer = root_client.get_all_layer()
	for ele in l_layer:
		root_client.delete_layer(ele["_id"])

	code, l_media = root_client.get_all_media()
	for ele in l_media:
		root_client.delete_media(ele["_id"])

	code, l_corpus = root_client.get_all_corpus()
	for ele in l_corpus:
		root_client.delete_corpus(ele["_id"])

	code, l_group = root_client.get_all_group()
	for ele in l_group:
		root_client.delete_group(ele["_id"])

	code, l_user = root_client.get_all_user()
	for ele in l_user:
		root_client.delete_user(ele["_id"])


if __name__ == '__main__':
	URL = "http://localhost:3000"

	root_client = camomile.client.CamomileClient('root', 'camomile', URL, False)
	print 'test authentification'
	empty_database(root_client)
	print 1, root_client.me()
	print 2, root_client.logout()
	print 3, root_client.login('truc', 'camomile')
	print 4, root_client.login('root', 'truc')
	print 5, root_client.login('root', 'camomile')

	print 'test user'
	data = {"username":"u1", "password":"u1_pwd", "description":{"test":"t"}, "role":"user"}
	code, u1 = root_client.create_user(data)
	print 101, (code, u1)
	data = {"password":"u2_pwd", "role":"user"}
	print 102, root_client.create_user(data)
	data = {"username":"u2", "role":"user"}
	print 103, root_client.create_user(data)
	data = {"username":"u2", "password":"u2_pwd"}
	print 104, root_client.create_user(data)	
	data = {"username":"u2", "password":"u2_pwd", "role":"truc"}
	print 105, root_client.create_user(data)
	print 106, root_client.get_user(u1['_id'])
	print 107, root_client.get_all_user()
	data = {"role":"admin"}
	print 108, root_client.update_user(u1['_id'], data)
	print 109, root_client.delete_user(u1['_id'])
	print 110, root_client.get_all_user()

	data = {"username":"u2", "password":"u2_pwd", "role":"user"}
	code, u2 = root_client.create_user(data)
	u2_client = camomile.client.CamomileClient('u2', 'u2_pwd', URL, False)

	data = {"username":"u3", "password":"u3_pwd", "description":{"test":"t"}, "role":"user"}
	code, u3 = u2_client.create_user(data)
	print 111, (code, u3)
	print 112, u2_client.get_user(u1['_id'])
	print 113, u2_client.get_all_user()

	data = {"username":"u4", "password":"u4_pwd", "description":{"test":"t"}, "role":"user"}
	code, u4 = root_client.create_user(data)	

	data = {"role":"admin"}
	print 114, u2_client.update_user(u4['_id'], data)
	print 115, u2_client.delete_user(u4['_id'])

	data = {"role":"admin"}
	print 116, root_client.update_user(u2['_id'], data)

	data = {"username":"u3", "password":"u3_pwd", "description":{"test":"t"}, "role":"user"}
	code, u3 = u2_client.create_user(data)
	print 117, (code, u3)
	print 118, u2_client.get_user(u1['_id'])
	print 119, u2_client.get_all_user()

	print 120, u2_client.logout()
	print 121, u2_client.login('u2', 'u2_pwd')

	code, u3 = u2_client.create_user(data)
	print 122, (code, u3)
	print 123, u2_client.get_user(u1['_id'])
	print 124, u2_client.get_user(u3['_id'])
	print 125, u2_client.get_all_user()

	print 'test group'
	data = {"name":"g1", "description":{"test":"t"}}
	code, g1 = root_client.create_group(data)
	print 201, (code, g1)
	data = {"description":{"test":"t"}}
	print 202, root_client.create_group(data)	
	print 203, root_client.get_group(g1['_id'])
	print 204, root_client.get_all_group()
	data = {"description":{"test":"t2"}}
	print 205, root_client.update_group(g1['_id'], data)
	print 206, root_client.delete_group(g1['_id'])
	print 207, root_client.get_all_group()

	data = {"name":"g2", "description":{"test":"t"}}
	code, g2 = root_client.create_group(data)

	print 208, root_client.add_user_to_a_group(g1["_id"], u3["_id"])
	print 209, root_client.add_user_to_a_group(g2["_id"], u1["_id"])
	print 210, root_client.add_user_to_a_group(g2["_id"], u3["_id"])
	root_client.add_user_to_a_group(g2["_id"], u4["_id"])

	print 211, root_client.get_group(g2['_id'])
	print 212, root_client.remove_user_to_a_group(g2["_id"], u3["_id"])
	print 213, root_client.remove_user_to_a_group(g2["_id"], u1["_id"])
	print 214, root_client.remove_user_to_a_group(g1["_id"], u3["_id"])
	print 215, root_client.remove_user_to_a_group(g2["_id"], u3["_id"])
	print 216, root_client.get_group(g2['_id'])

	print 217, root_client.get_all_group_of_a_user(u3['_id'])
	root_client.add_user_to_a_group(g2["_id"], u3["_id"])
	data = {"name":"g3"}
	code, g3 = root_client.create_group(data)
	root_client.add_user_to_a_group(g3["_id"], u3["_id"])
	print 218, root_client.get_all_group_of_a_user(u3['_id'])


	print 'test corpus'
	data = {"name":"u1", "description":{"test":"t"}}
	code, c1 = root_client.create_corpus(data)
	print 301, (code, c1)
	data = {"description":{"test":"t"}}
	print 302, root_client.create_corpus(data)	
	print 303, root_client.get_corpus(c1['_id'])
	print 304, root_client.get_all_corpus()
	print 305, root_client.update_corpus(c1['_id'], data)
	print 306, root_client.delete_corpus(c1['_id'])
	print 307, root_client.get_all_corpus()

	data = {"name":"c2"}
	code, c2 = root_client.create_corpus(data)

	data = {"name":"m1", "url":"...", "description":{"t":"..."}}
	print 308, root_client.add_media(c1['_id'], data)	
	data = {"url":"...", "description":{"...":"..."}}
	print 309, root_client.add_media(c2['_id'], data)
	data = {"name":"m1", "url":"...", "description":{"t":"..."}}
	code, m1 = root_client.add_media(c2['_id'], data)
	print 310, (code, m1)
	data = {"name":"m2", "url":"...", "description":{"t":"..."}}
	code, m2 = root_client.add_media(c2['_id'], data)
	print 311, root_client.get_all_media_of_a_corpus(c2['_id'])

	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	print 312, root_client.add_layer(c1['_id'], data)	
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	print 313, root_client.add_layer(c2['_id'], data)
	data = {"description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	print 314, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "data_type":{"t":"t"}}
	print 315, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}}
	print 316, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	code, l1 = root_client.add_layer(c2['_id'], data)
	print 317, (code, l1)
	data = {"name":"l2", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	code, l2 = root_client.add_layer(c2['_id'], data)
	print 318, root_client.get_all_layer_of_a_corpus(c2['_id'])
	








