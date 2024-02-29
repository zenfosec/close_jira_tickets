#! /usr/bin/env python3

from jira import JIRA

options = {
    'server': 'https://yourjiraserver.yourdomain.com/'
}

# replace user.name and password with your own
jira = JIRA(options, basic_auth=('user.name', 'password'))

# replace the query with your own
query = 'project = "PROJECT" AND summary ~ "This is the text it will search for" AND status != Resolved'
issues = jira.search_issues(query)

for issue in issues:
    transitions = jira.transitions(issue)
    for transition in transitions:
        if transition['to']['name'] == 'In Progress':
            jira.transition_issue(issue, transition['id'])
            break
    
    transitions = jira.transitions(issue)
    for transition in transitions:
        if transition['to']['name'] == 'Resolved':
            jira.transition_issue(issue, transition['id'])
            break
    # issue.update(fields={'status': 'Complete'})

    # replace the comment with your own
    comment = jira.add_comment(issue.key, 'PUT COMMENT HERE')
    print(issue.key, "has been resolved")