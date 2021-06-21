#A Multi-Tenancy Django Demo

This demo follows a semi-isolated approach to handling multi-tenancy by using one database but, segregated schemas for tenant data.
Built using the django-tenant-schemas library, this demo should demonstrate how to isolate data and direct requests based on tenant information such as subdomain or HTTP header.

Most SAAS applications require multi-tenancy in some form in order to offer their services to more than one client. There seems to be two areas of special interest when applying an MT architecture to Django:
* Authentication and Authorisation
* Data isolation

# Data isolation:
Multi-tenancy data isolation can be solved with three solutions:
###* Isolated Approach
Separate databases. Each tenant has it's own database
###* Semi-Isolated Approach
Shared DB, separated schemas. Tenants share the same database but isolation is achieved through tenant dedicated schemas.
###* Shared Approach
Shared database, shared schema. All tenants share the same database and schema. There is a main tenant-table where all other tables have a 
foreign key pointing to a tenant_id. Database schema is the default 'public' schema.

# Postgres Schemas
More information about how Postgres creates and handles schemas can be found here: https://www.postgresql.org/docs/9.2/ddl-schemas.html
By default, Django will use the public Postgres schema. TENANT_APPS will have their own schema whereas SHARED_APPS will be written to the public schema.
Integrating the django-tenant-schema (DTS) library massively simplifies developing Django to gracefully handle many, many DB schemas without 
disrupting the development experience. In short, DTS will handle a lot of the 'heavy lifting' needed to quickly build a SAAS/M.T. application
so that you can just focus on building out the rest of the project.
DTS also provides some handy tools to aid the development process including a context manager to select between which schema(s) you want to interact with 
as well as a set of test cases that automatically point tests towards a tenants domain. 

# Running the project

### Never use migrate as it would sync all your apps to public!
$ python manage.py migrate_schemas --shared

