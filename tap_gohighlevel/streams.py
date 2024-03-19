"""Stream type classes for tap-gohighlevel."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_gohighlevel.client import GoHighLevelStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"

class ContactsStream(GoHighLevelStream):
    """Contacts stream."""

    name = "contacts"
    path = "contacts/"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.contacts[*]"
    # TODO: verify this
    replication_key = "dateUpdated"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("locationId", th.StringType),
        th.Property("businessId", th.StringType),
        th.Property("attributions", th.ArrayType(th.ObjectType())),
        th.Property("followers", th.StringType),
        th.Property("email", th.StringType),
        th.Property("country", th.StringType),
        th.Property("dndSettings", th.ObjectType()),
        th.Property("additionalEmails", th.ArrayType(th.StringType)),
        th.Property("source", th.StringType),
        th.Property("dateAdded", th.DateTimeType),
        th.Property(
            "customFields",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("value", th.StringType),
                )
            ),
        ),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("phone", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("contactName", th.StringType),
        th.Property("companyName", th.StringType),
        th.Property("type", th.StringType),
        th.Property("dnd", th.BooleanType),
        th.Property("assignedTo", th.StringType),
        th.Property("city", th.StringType),
        th.Property("state", th.StringType),
        th.Property("postalCode", th.StringType),
        th.Property("address1", th.StringType),
        th.Property("dateUpdated", th.DateTimeType),
        th.Property("dateOfBirth", th.StringType),

    ).to_dict()

