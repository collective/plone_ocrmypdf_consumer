plone_ocrmypdf_consumer
-----------------------

This package provides a consumer client for `collective.ocrmypdf <https://github.com/collective/collective.ocrmypdf>`_ offering OCR functionality for PDF files in Plone. It enables automated document processing, integrated with Redis for task communication.


Installation
------------

Install this package using pip::

    pip install plone_ocrmypdf_consumer

Usage
-----

1. **Configure Environment Variables**:
    - **REDIS_HOST**: The hostname for your Redis server (e.g., ``redis``).
    - **REDIS_PORT**: The port number for your Redis server (e.g., ``6379``).
    - **REDIS_CHANNEL**: The Redis channel for listening to OCR tasks (e.g., ``ocr_tasks``).
    - **API_URL**: The base URL of your Plone CMS instance (e.g., ``http://backend:8080/Plone``)
    - **API_USERNAME** and **API_PASSWORD**: Credentials for Plone API authentication.



2. **Integration with Plone**:
    - Ensure collective.ocrmypdf is installed in your Plone instance.


Development
-----------

To set up the development environment::

    git clone https://github.com/collective/plone_ocrmypdf_consumer.git
    cd plone_ocrmypdf_consumer
    pip install -e .


Contributing
------------

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
See the CONTRIBUTING file for details.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
