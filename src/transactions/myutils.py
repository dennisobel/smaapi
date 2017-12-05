
class Countries():
	country = {
		"Belgium":{"currency":"Euro","flag":"assets/flags-big/cd.png"},
		"Canada":{"currency":"CAN$","flag":"assets/flags-big/ca.png"},
		"France":{"currency":"Euro","flag":"assets/flags-big/fr.png"},
		"Denmark":{"currency":"Euro","flag":"assets/flags-big/be.png"},
		"Sweden":{"currency":"Euro","flag":"assets/flags-big/ng.png"}
	}

	for k1,v1 in country.iteritems():
		for k2,v2 in v1.iteritems():			
			countries = k1
			currency = k2
			flag = v2
			
		
