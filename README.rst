##########
django VMS
##########

VMS(Video Management System) is a simple video management system based on the django framework.

Detailed documentation is in the "docs" directory.

********
Features
********

* support admin page for management video
* using `Elasticsearch <https://www.elastic.co/products/elasticsearch>`_ for store and explore video

********
Quick start
********

1. Add "vms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
            ...
            'vms',
    )

2. Include the vms URLconf in your project urls.py like this::

    url(r'^vms/', include('vms.urls')),

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to use vms (you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/vms/ to participate in the vms.
