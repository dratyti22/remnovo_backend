# Tags

information about tag

    Create - Employees
    Update - Employees
    Delete - Employees
    Watch - Everything

## Path:

    /api/tag/

### Example of the data that is coming in:

    {
        "id": 1,
        "user": 1,
        "section": false,
        "name": "a",
        "parent": null,
        "time_create": 1718613581
    },
    {
        "id": 3,
        "user": 1,
        "section": false,
        "name": "aaaaa",
        "parent": 1,
        "time_create": 1718881237
    },

### Data to be sent:

    {
        "section": false,
        "name": "",
        "parent": null
    }

#### Description of fields

id: A unique tag identifier. \
user: The ID of the user who created the tag is created automatically. \
section: A flag indicating whether the tag is a section (initially false). \
name: The name of the tag. \
parent: ID of the parent tag (null if there is no parent). \
time_create: Time of tag creation (automatically created in the database). \

#### Search

    /api/tag/?search=

Fields:

    name 
    user__id