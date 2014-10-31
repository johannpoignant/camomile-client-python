import camomile.client
import json

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

def print_r(r):
	for key in sorted(r):
		if key=="history":
			print "     history:[",
			for h in r[key]:
				print h, ',\n              ',
			print ']'
		else:
			print '    ', key+':', r[key]
	print

def print_ACL(ACL):
	if 'users' in ACL['ACL']:
		print '   users:'
		for user in ACL['ACL']['users']:
			print "    ", user, ACL['ACL']['users'][user]
	if 'groups' in ACL['ACL']:
		print '   groups:'
		for group in ACL['ACL']['groups']:
			print "    ", group, ACL['ACL']['groups'][group]	


if __name__ == '__main__':
	URL = "http://localhost:3000"

	root_client = camomile.client.CamomileClient('root', 'camomile', URL, False)
	empty_database(root_client)


	data = {"name":"corpus1", "description":{"abc":"def"}}
	code, c1 = root_client.create_corpus(data)
	data = {"name":"media1", "url":"url_media1", "description":{"abc":"def"}}
	code, m1 = root_client.add_media(c1['_id'], data)

	data = {"name":"layer1", "description":{"abc":"def"}, "fragment_type":"segment", "data_type":"name"}
	code, l1 = root_client.add_layer(c1['_id'], data)

	data = {"id_media":m1['_id'], "fragment":"fragment1", "data":"data1"}
	code, a1 = root_client.add_annotation(l1['_id'], data)
	data = {"id_media":m1['_id'], "fragment":"fragment2", "data":"data2"}
	code, a1 = root_client.add_annotation(l1['_id'], data)
	

	code, val = root_client.get_all_annotation_of_a_layer(l1['_id'])



	print json.dumps(val, indent=2, sort_keys=True)




	'''
	print 'test authentification'
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
	code, l_u = root_client.get_all_user()
	print 107, code
	for u in l_u:
		print_r(u)

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
	code, l_u = u2_client.get_all_user()
	print 125, code
	for u in l_u:
		print_r(u)

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
	code, l_g = root_client.get_all_group_of_a_user(u3['_id'])
	print 218, code
	for g in l_g:
		print_r(g)

	print 'test corpus'
	data = {"name":"u1", "description":{"test":"t"}}
	code, c1 = root_client.create_corpus(data)
	print 301, code
	print_r(c1)
	data = {"description":{"test":"t"}}
	print 302, root_client.create_corpus(data)	
	code, c1 = root_client.get_corpus(c1['_id'])
	print 303, code
	print_r(c1)
	code, l_c = root_client.get_all_corpus()
	print 304, code
	for c in l_c:
		print_r(c)
	code, c1 = root_client.update_corpus(c1['_id'], data)
	print 305, code
	print_r(c1)
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
	print 310, code
	print_r(m1)
	data = {"name":"m2", "url":"...", "description":{"t":"..."}}
	code, m2 = root_client.add_media(c2['_id'], data)
	code, l_m = root_client.get_all_media_of_a_corpus(c2['_id'])
	print 311, code
	for m in l_m:
		print_r(m)

	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	print 312, root_client.add_layer(c1['_id'], data)	
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	code, l = root_client.add_layer(c2['_id'], data)
	print 313, code
	print_r(l) 
	data = {"description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	print 314, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "data_type":{"t":"t"}}
	print 315, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}}
	print 316, root_client.add_layer(c2['_id'], data)
	data = {"name":"l1", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	code, l1 = root_client.add_layer(c2['_id'], data)
	print 317, code
	print_r(l1)
	data = {"name":"l2", "description":{"t":"t"}, "fragment_type":{"t":"t"}, "data_type":{"t":"t"}}
	code, l2 = root_client.add_layer(c2['_id'], data)
	print 318, code
	code, l_l = root_client.get_all_layer_of_a_corpus(c2['_id'])
	for l in l_l:
		print_r(l)

	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 319, code
	print_ACL(ACL)

	print 320, root_client.update_user_ACL_of_a_corpus(c2['_id'], u2['_id'], {"Right":"faux"})
	print 321, root_client.update_user_ACL_of_a_corpus(c1['_id'], u2['_id'], {"Right":"R"})
	print 322, root_client.update_user_ACL_of_a_corpus(c2['_id'], u1['_id'], {"Right":"R"})
	print 323, root_client.update_user_ACL_of_a_corpus(c2['_id'], u2['_id'], {"Right":"R"})
	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 324, code
	print_ACL(ACL)

	print 325, root_client.update_group_ACL_of_a_corpus(c2['_id'], g3['_id'], {"Right":"faux"})
	print 326, root_client.update_group_ACL_of_a_corpus(c1['_id'], g3['_id'], {"Right":"R"})
	print 327, root_client.update_group_ACL_of_a_corpus(c2['_id'], g1['_id'], {"Right":"R"})
	print 328, root_client.update_group_ACL_of_a_corpus(c2['_id'], g3['_id'], {"Right":"R"})
	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 329, code
	print_ACL(ACL)

	print 330, u2_client.update_user_ACL_of_a_corpus(c2['_id'], u4['_id'], {"Right":"R"})
	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 331, code
	print_ACL(ACL)

	print 332, root_client.update_user_ACL_of_a_corpus(c2['_id'], u2['_id'], {"Right":"W"})
	print 333, u2_client.update_user_ACL_of_a_corpus(c2['_id'], u4['_id'], {"Right":"R"})
	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 334, code
	print_ACL(ACL)

	print 332, root_client.update_user_ACL_of_a_corpus(c2['_id'], u2['_id'], {"Right":"O"})
	print 333, u2_client.update_user_ACL_of_a_corpus(c2['_id'], u4['_id'], {"Right":"R"})
	code, ACL = root_client.get_ACL_of_a_corpus(c2['_id'])
	print 334, code
	print_ACL(ACL)
	'''






	empty_database(root_client)	


