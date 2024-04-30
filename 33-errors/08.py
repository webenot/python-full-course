def image_info(image):
    if ('image_title' not in image) or ('image_id' not in image):
        raise TypeError('Keys image_title or image_id not found in input dictionary')
    return f"Image '{image['image_title']}' has id {image['image_id']}"


try:
    print(image_info({'image_title': 'Test image'}))
except TypeError as e:
    print(e)
