# File

information about the file

    Create - Registered and admin
    Update-owner or employee
    Delete-the owner or the employee
    Watch-Everything

## Path:

    /api/file/

### Example of the data that is coming in:

    {
        "filename": "F",
        "height": 100.0,
        "width": 100.0,
        "length": 100.0,
        "status": 1,
        "owners": [
            1
        ],
        "materials": [
            1
        ],
        "time_create": 1718613635
    },

### Data to be deleted:

    {
        "filename": "",
        "height": null,
        "width": null,
        "length": null,
        "status": null,
        "materials": []
    }

#### Description of the field

filename: A unique name for the file \
height: Height. \
Width. \
Length: Length. \
status: A number from 0 to 3 each number displays an indicator:

    (0, 'not checked'),
    (1, 'active'),
    (2, 'banned'),
    (3, 'cannot be deleted or disabled'). 

owners: Who owns, automatically. \
materials: What kind of material, delete id

#### Search

    /api/file/?search=

Fields:

    status 
    time_create 
    owners__id