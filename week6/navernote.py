def extract_info(naverbook_list) : 
    result = []
    for note in naverbook_list:
        title = note.find("a",{"class" : "N=a:bta.title"}).string
        img_src = note.find("div", {"class" : "thumb_type thumb_type2"}).find("img")['src']
        link = note.find("div", {"class" : "thumb_type thumb_type2"}).find("a")['href']
        author = note.find("dd", {"class" : "txt_block"}).find("a", {"class" : "txt_name N=a:bta.author"}).string
        publisher = note.find("dd", {"class" : "txt_block"}).find("a", {"class" : "N=a:bta.publisher"}).string
        note_info = {
            "title" : title,
            "img_src" : img_src,
            "link" : link,
            "author" : author,
            "publisher" : publisher
        }
        result.append(note_info)
    return result