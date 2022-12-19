import config

def main(data, workflow):
	try:
		salestekker_id = data['application_custom_text1']
		stage_name = data['application_stage']
		stages = workflow['data']['workflow']['stages']
		sfg_stage = [i for i in config.SFG_CHECKER if i == stage_name][0]
		for stage in stages:
			if stage['name'] == stage_name:
				if stage['id'] == sfg_stage['SFG_ID']:
					return sfg_stage
		return False
	except Exception as e:
		print(e)
		return False