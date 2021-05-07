import asyncio
import re
from pathlib import Path

from aiograph import Telegraph

# example_content = '<p>Page created by <a href="https://github.com/aiogram/aiograph" target="_blank">AIOGraph</a></p>' \
#           '<img src="{image}"/>' \
#           '<h4 id="Lorem-ipsum">Lorem ipsum</h4>' \
#           '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ' \
#           'ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco ' \
#           'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in vol ' \
#           'uptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non ' \
#           'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p> ' \
#           '<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, ' \
#           'totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae ' \
#           'dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, ' \
#           'sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam ' \
#           'est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius ' \
#           'modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, ' \
#           'quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi ' \
#           'consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil ' \
#           'molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</p> ' \
#           '<p><h4 id="FooBar">FooBar</h4><ul><li>Foo</li><li>Bar</li><li>Baz</li></ul></p>'
def htmlification_msg(msg:str):
    before_editing = msg
    find_header = re.findall(r'\((.*?)\)h',before_editing)#
    for i in range(len(find_header)):
        before_editing = before_editing.replace('(%s)h'% find_header[i],'<h4>%s</h4>' % find_header[i])

    find_header = re.findall(r'\((.*?)\)b',before_editing)#
    for i in range(len(find_header)):
        before_editing = before_editing.replace('(%s)b'% find_header[i],'<b>%s</b>' % find_header[i])

    find_header = re.findall(r'\((.*?)\)p', before_editing)
    for i in range(len(find_header)):
        before_editing = before_editing.replace('(%s)p' % find_header[i], '<p>%s</p>' % find_header[i])

    find_header = re.findall(r'\((.*?)\)l',before_editing)
    for i in range(len(find_header)):
        if i == 0:
            before_editing = before_editing.replace('(%s)l' % find_header[i], '<p><ul><li>%s</li>' % find_header[i])
        elif i == len(find_header)-1:
            before_editing = before_editing.replace('(%s)l' % find_header[i], '<li>%s</li></ul></p>' % find_header[i])
        else:
            before_editing = before_editing.replace('(%s)l'% find_header[i],'<li>%s</li>' % find_header[i])

    after_editing = before_editing.replace('\n','').replace('\r','')
    print(after_editing)

    return after_editing + '<img src="{image}"/>'



async def main(cap:str=None, desc:str=None, img_path:str=None ):
    telegraph = Telegraph()

    await telegraph.create_account('aiograph-demo')
    to_html_content = htmlification_msg(desc)
    photo = (await telegraph.upload(img_path, full=False))[0]
    page_content = to_html_content.format(image=photo)
    page = await telegraph.create_page(cap, page_content)
    print('Created page:', page.url)

    await telegraph.close()# Close the aiohttp.ClientSession

    return page.url


