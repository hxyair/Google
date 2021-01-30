names=["Calos","Ray","Hans","Alex","Kelly"]
print(sorted(names,key=len))

def get_event_date(event):
	return event.date

def current_users(events):
	events.sort(key=get_event_date)
	machines={}
	for event in events:
		if event.machine not in machines:
			machines[event.machine]=set()
		if event.type ="login":
			machines[event.machine].add(event.user)
		elif event.type="logout":
			machines[event.machine].remove(event.user)
	return machines

def generate_report(machines):
	for machine,users in machines.items():
		if len(users)>0:
			user_list=", ".joint(users)
			print('{}: {}'.format(machine, user_list))


'''
This final project is the real test of how much you've gotten your head around and can highlight areas you need to brush up on. So we want you to be super clear on what you need to do on that point. You'll find an overview of what you have to do in the next reading. Can you guess the best way of tackling this problem? Yep, you got it, our step-by-step approach that we outlined earlier. Understand the problem statement, research available options, plan your approach, write your code and finally execute. Okay, feeling good? Ready to go? Remember, you know this stuff and you've totally got it.
'''