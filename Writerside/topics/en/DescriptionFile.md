# DescriptionFile

information about DescriptionFile

    Create - file owner and admin
    Update - file owner and admin
    Delete - file owner and admin
    Watch - Everything

## Path:

    /api/description/file/

### Example of the data that is coming in:

    {
        "pk": 3,
        "file": "f",
        "user_id": 2,
        "title": "uuu",
        "description": "uu",
        "line_video": "https://yootube.com/uuu ",
        "tags": [
            1
        ],
        "image_file": [
            {
                "image": "http://localhost:8000/media/file_image/biker-digital-art-butterflies-uhdpaper.com-4K-6.1044_YbhOmDk.jpg"
            }
        ],
        "time_create": 1718810317
    },

### Data to be sent:

    {
        "file": "",
        "title": '',
        "description": '',
        "line_video": '',
        "tags": [],
        "uploaded_images": []
    }

#### Description of fields

file: A unique name for the file \
title: The title. \
description: Description. \
line_video: Link to the video. \
tags: A list of which tags are linked to, id tags
uploaded_images: Photo
User: Created automatically

#### Information about creation

    If you create it with a photo, then use multipart/form-data
    If without a photo, then you can use json

    You can update json without photos
    With photo by multipart/form-data

#### Search

    /api/description/file/?search=

Fields:

    time_create 
    user__id 
    tags__name