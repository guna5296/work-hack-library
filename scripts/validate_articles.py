import json, pathlib, sys
p=pathlib.Path('data/articles.json')
try: data=json.loads(p.read_text(encoding='utf-8'))
except Exception as e: print(f'Invalid JSON: {e}'); sys.exit(1)
required=['id','title','category','summary','sourceTitle','sourceUrl','updated','sections']
ids=set()
for i,a in enumerate(data):
    missing=[k for k in required if not a.get(k)]
    if missing: print(f"Article #{i+1} ({a.get('id','?')}): missing {', '.join(missing)}")
    if a.get('id') in ids: print(f"Duplicate id: {a.get('id')}")
    ids.add(a.get('id'))
    if a.get('sourceUrl') and not a['sourceUrl'].startswith(('https://','http://')): print(f"Invalid source URL: {a.get('id')}")
    if a.get('quiz'):
        q=a['quiz']; opts=q.get('options',[])
        if not opts or not isinstance(q.get('answer'),int) or q['answer']<0 or q['answer']>=len(opts): print(f"Invalid quiz: {a.get('id')}")
print(f'Validated {len(data)} article records.')
