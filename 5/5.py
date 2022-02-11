import xml.dom.minidom

dom = xml.dom.minidom.parse("demo.xml")
template = dom.getElementsByTagName('template')

for template_item in template:
    print('Attribute: ', template_item.getAttribute('id'))
    print('Tag: ', template_item.tagName)

    for xpath in template_item.childNodes:
        if xpath.nodeType == xpath.ELEMENT_NODE:
            position = xpath.getAttribute("position")
            print("Attribute: position: ", position)
            print("Tag Name: ", xpath.tagName)

            for child_tags in xpath.childNodes:
                if child_tags.nodeType == child_tags.ELEMENT_NODE:
                    if child_tags.tagName == "link":
                        href = child_tags.getAttribute("href").split("/")[-1]
                        print("Attribute: href: ", href)
                        print("Tag Name: ", child_tags.tagName)

                    else:
                        src = child_tags.getAttribute("src").split("/")[-1]
                        print("Attribute: src: ", src)
                        print("Tag Name:", child_tags.tagName)


