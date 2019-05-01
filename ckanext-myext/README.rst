=============
ckanext-myext
=============

A very simple Hello World plugin that:

- Updates the Home Page promoted text template with a Hello World message.
- 

------------
Requirements
------------

Works with CKAN 2.8. Plug and play!

------------
Installation
------------

To install ckanext-myext:

1. Add ``myext`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

2. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

# The message which will appear in the heading of the promoted 
# on the home page
ckanext.myext.home_promoted_message = "Hello World"


------------------------
Development Installation
------------------------

To install ckanext-myext for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/starsinmypockets/ckanext-myext.git
    cd ckanext-myext
