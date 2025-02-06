def buildMenu(edgeNodes):

	menu = []
	
	home = {
	  "target": "/",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "Home",
	    "icon": {
	      "path": "material/home",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(home)
	
	monthlyPeak = {
	  "target": "/monthlypeak",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "Monthly Peak",
	    "icon": {
	      "path": "material/show_chart",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(monthlyPeak)
		
	history = {
	  "target": "/history",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "History",
	    "icon": {
	      "path": "material/show_chart",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(history)
	
	deviceCount = 0
	
#	for i in edgeNodes:
#		
#		edgeNode = {
#			  "target": "/",
#			  "items": [],
#			  "navIcon": {"path": "material/chevron_right","color": "#000F5D"},
#			  "label": {
#			    "text": i.name,
#			    "icon": {
#			      "path": "material/device_hub",
#			      "color": "#000F5D"
#			    }
#			  },
#			  "showHeader": False,
#			  "style": {
#			    "classes": "",
#			    "fontWeight": "bold"
#			  }
#			}
#		
#
#		for d in i["energyLoads"][deviceCount]:
##			typeId = d.typeId.split("/")[len(d.typeId.split("/"))-1]
#			typeId = d.typeId
#			device = {
#				  "target": "/energy-device/" + i.name + "/" + d.name + "/" + typeId,
#				  "items": [],
#				  "navIcon": {},
#				  "label": {
#				    "text": d.name,
#				    "icon": {
#				      "path": "material/offline_bolt",
#				      "color": "#000F5D"
#				    }
#				  },
#				  "showHeader": False,
#				  "style": {
#				    "classes": "",
#				    "fontWeight": "bold"
#				  }
#				}
#			edgeNode['items'].append(device)
#		deviceCount = deviceCount + 1
#		
#		menu.append(edgeNode)
		
	return menu
	
def buildMenu_OLD(edgeNodes):
	

	menu = []
	
	home = {
	  "target": "/",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "Home",
	    "icon": {
	      "path": "material/home",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(home)
	
	monthlyPeak = {
	  "target": "/monthlypeak",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "Monthly Peak",
	    "icon": {
	      "path": "material/show_chart",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(monthlyPeak)
		
	history = {
	  "target": "/history",
	  "items": [],
	  "navIcon": {},
	  "label": {
	    "text": "History",
	    "icon": {
	      "path": "material/show_chart",
	      "color": "#000F5D"
	    }
	  },
	  "showHeader": False,
	  "style": {
	    "classes": "",
	    "fontWeight": "bold"
	  }
	}
	menu.append(history)
	
	deviceCount = 0
	
	for i in edgeNodes:
		
		edgeNode = {
			  "target": "/",
			  "items": [],
			  "navIcon": {"path": "material/chevron_right","color": "#000F5D"},
			  "label": {
			    "text": i.name,
			    "icon": {
			      "path": "material/device_hub",
			      "color": "#000F5D"
			    }
			  },
			  "showHeader": False,
			  "style": {
			    "classes": "",
			    "fontWeight": "bold"
			  }
			}
		

		for d in i["energyLoads"][deviceCount]:
			typeId = d.typeId.split("/")[len(d.typeId.split("/"))-1]
		
			device = {
				  "target": "/energy-device/" + i.name + "/" + d.name + "/" + typeId,
				  "items": [],
				  "navIcon": {},
				  "label": {
				    "text": d.name,
				    "icon": {
				      "path": "material/offline_bolt",
				      "color": "#000F5D"
				    }
				  },
				  "showHeader": False,
				  "style": {
				    "classes": "",
				    "fontWeight": "bold"
				  }
				}
			edgeNode['items'].append(device)
		deviceCount = deviceCount + 1
		
		menu.append(edgeNode)
		
	return menu
