"""Stream type classes for tap-gohighlevel."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_gohighlevel.client import GoHighLevelStream


class ContactsStream(GoHighLevelStream):
    """Contacts stream."""

    name = "contacts"
    path = "contacts/"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.contacts[*]"
    replication_key = "dateUpdated"
    api_version = "2021-07-28"

    def _get_default_params(self, context) -> dict | None:
        return {
            "limit": 100,
            "locationId":  self.config.get("location_id"),
        }

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

class CalendarsStream(GoHighLevelStream):
    """Calendars stream."""

    name = "calendars"
    path = "calendars/"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.calendars[*]"
    api_version = "2021-04-15"

    def _get_default_params(self, context) -> dict | None:
        return {
            "locationId":  self.config.get("location_id"),
        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("notifications", th.ArrayType(th.ObjectType())),
        th.Property("locationId", th.StringType),
        th.Property("groupId", th.StringType),
        th.Property("teamMembers", th.ArrayType(th.ObjectType())),
        th.Property("eventType", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("widgetSlug", th.StringType),
        th.Property("calendarType", th.StringType),
        th.Property("widgetType", th.StringType),
        th.Property("eventTitle", th.StringType),
        th.Property("eventColor", th.StringType),
        th.Property("meetingLocation", th.StringType),
        th.Property("slotDuration", th.IntegerType),
        th.Property("preBufferUnit", th.StringType),
        th.Property("slotInterval", th.IntegerType),
        th.Property("slotBuffer", th.IntegerType),
        th.Property("preBuffer", th.IntegerType),
        th.Property("appoinmentPerSlot", th.IntegerType),
        th.Property("appoinmentPerDay", th.IntegerType),
        th.Property("openHours", th.ArrayType(th.ObjectType())),
        th.Property("enableRecurring", th.BooleanType),
        th.Property("recurring", th.ObjectType()),
        th.Property("formId", th.StringType),
        th.Property("stickyContact", th.BooleanType),
        th.Property("isLivePaymentMode", th.BooleanType),
        th.Property("autoConfirm", th.BooleanType),
        th.Property("shouldSendAlertEmailsToAssignedMember", th.BooleanType),
        th.Property("alertEmail", th.StringType),
        th.Property("googleInvitationEmails", th.BooleanType),
        th.Property("allowReschedule", th.BooleanType),
        th.Property("allowCancellation", th.BooleanType),
        th.Property("shouldAssignContactToTeamMember", th.BooleanType),
        th.Property("shouldSkipAssigningContactForExisting", th.BooleanType),
        th.Property("notes", th.StringType),
        th.Property("pixelId", th.StringType),
        th.Property("formSubmitType", th.StringType),
        th.Property("formSubmitRedirectURL", th.StringType),
        th.Property("formSubmitThanksMessage", th.StringType),
        th.Property("availabilityType", th.IntegerType),
        th.Property("availabilities", th.ArrayType(th.ObjectType())),
        th.Property("guestType", th.StringType),
        th.Property("consentLabel", th.StringType),
        th.Property("calendarCoverImage", th.StringType),
    ).to_dict()


class OpportunitiesStream(GoHighLevelStream):
    """Opportunities stream."""

    # https://highlevel..io/docs/integrations/a163e98c45b8d-search-opportunity
    name = "opportunities"
    path = "opportunities/search"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.opportunities[*]"
    api_version = "2021-07-28"

    def _get_default_params(self, context) -> dict | None:
        return {
            "limit": 100,
            "getCalendarEvents": "true",
            "getNotes": "true",
            "getTasks": "true",
            "location_id":  self.config.get("location_id"),
            # "status": "all",
            # "order": "added_asc"
            # "date": "01-01-2021"
        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("monetaryValue", th.IntegerType),
        th.Property("pipelineId", th.StringType),
        th.Property("pipelineStageId", th.StringType),
        th.Property("assignedTo", th.StringType),
        th.Property("status", th.StringType),
        th.Property("source", th.StringType),
        th.Property("lastStatusChangeAt", th.DateTimeType),
        th.Property("lastStageChangeAt", th.DateTimeType),
        th.Property("lastActionDate", th.DateTimeType),
        th.Property("indexVersion", th.IntegerType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("contactId", th.StringType),
        th.Property("locationId", th.StringType),
        th.Property("contact", th.ObjectType()),
        th.Property("notes", th.ArrayType(th.StringType)),
        th.Property("tasks", th.ArrayType(th.StringType)),
        th.Property("calendarEvents", th.ArrayType(th.StringType)),
        th.Property("customFields", th.ArrayType(th.ObjectType())),
        th.Property("followers", th.ArrayType(th.ArrayType(th.ObjectType()))),
        th.Property("pipelineStageUId", th.StringType),
        th.Property("lostReasonId", th.StringType),
        th.Property("calenders", th.ArrayType(th.StringType)),
    ).to_dict()

class BusinessesStream(GoHighLevelStream):
    """Businesses stream."""

    # https://highlevel.stoplight.io/docs/integrations/a8db8afcbe0a3-get-businesses-by-location
    name = "businesses"
    path = "businesses/"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.businesses[*]"
    api_version = "2021-04-15"

    def _get_default_params(self, context) -> dict | None:
        return {
            "locationId": self.config.get("location_id"),
        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("email", th.StringType),
        th.Property("website", th.StringType),
        th.Property("address", th.StringType),
        th.Property("city", th.StringType),
        th.Property("description", th.StringType),
        th.Property("state", th.StringType),
        th.Property("postalCode", th.StringType),
        th.Property("country", th.StringType),
        th.Property("updatedBy", th.ObjectType()),
        th.Property("locationId", th.StringType),
        th.Property("createdBy", th.ObjectType()),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType)
    ).to_dict()


class ConversationsStream(GoHighLevelStream):
    """Conversations stream."""

    # https://highlevel.stoplight.io/docs/integrations/d45ae3189eea8-search-conversations
    name = "conversations"
    path = "conversations/search"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.conversations[*]"
    api_version = "2021-04-15"

    def _get_default_params(self, context) -> dict | None:
        return {
            "limit": 100,
            "locationId":  self.config.get("location_id"),
            # "status": "all",
            # "sortBy": last_manual_message_date last_message_date score_profile

        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("contactId", th.StringType),
        th.Property("locationId", th.StringType),
        th.Property("lastMessageBody", th.StringType),
        th.Property("lastMessageType", th.StringType),
        th.Property("type", th.StringType),
        th.Property("unreadCount", th.IntegerType),
        th.Property("fullName", th.StringType),
        th.Property("contactName", th.StringType),
        th.Property("email", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("dateAdded", th.DateTimeType),
        th.Property("dateUpdated", th.DateTimeType),
        th.Property("lastMessageDate", th.DateTimeType),
        th.Property("companyName", th.StringType),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("scoring", th.ArrayType(th.StringType)),
        th.Property("attributed", th.BooleanType),
        th.Property("sort", th.ArrayType(th.IntegerType)),
    ).to_dict()


class LocationStream(GoHighLevelStream):
    """Location stream."""

    # https://highlevel.stoplight.io/docs/integrations/d777490312af4-get-location
    name = "location"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.location[*]"
    api_version = "2021-07-28"

    def get_child_context(self, record: dict, context: dict | None) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "companyId": record["companyId"],
        }

    def _get_default_params(self, context) -> dict | None:
        return {
            "limit": 10,
            # "order": "added_asc"
        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("email", th.StringType),
        th.Property("address", th.StringType),
        th.Property("city", th.StringType),
        th.Property("state", th.StringType),
        th.Property("country", th.StringType),
        th.Property("postalCode", th.StringType),
        th.Property("website", th.StringType),
        th.Property("timezone", th.StringType),
        th.Property("settings", th.ObjectType()),
        th.Property("social", th.ObjectType()),
        th.Property("companyId", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("automaticMobileAppInvite", th.BooleanType),
        th.Property("dateAdded", th.DateTimeType),
        th.Property("domain", th.StringType),
    ).to_dict()



class UsersStream(GoHighLevelStream):
    """Conversations stream."""

    # https://highlevel.stoplight.io/docs/integrations/6fac93869cd3f-search-users
    name = "users"
    path = "users/search"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.users[*]"
    api_version = "2021-07-28"
    parent_stream_type = LocationStream

    def _get_default_params(self, context) -> dict | None:
        return {
            "limit": 100,
            "locationId":  self.config.get("location_id"),
            "companyId": context["companyId"]
            # "status": "all",
            # "sortBy": last_manual_message_date last_message_date score_profile

        }

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("companyId", th.StringType),
        th.Property("email", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("extension", th.StringType),
        th.Property("permissions", th.ObjectType(
            th.Property("adwordsReportingEnabled", th.BooleanType),
            th.Property("affiliateManagerEnabled", th.BooleanType),
            th.Property("agentReportingEnabled", th.BooleanType),
            th.Property("appointmentsEnabled", th.BooleanType),
            th.Property("assignedDataOnly", th.BooleanType),
            th.Property("attributionsReportingEnabled", th.BooleanType),
            th.Property("bloggingEnabled", th.BooleanType),
            th.Property("botService", th.BooleanType),
            th.Property("bulkRequestsEnabled", th.BooleanType),
            th.Property("campaignsEnabled", th.BooleanType),
            th.Property("campaignsReadOnly", th.BooleanType),
            th.Property("cancelSubscriptionEnabled", th.BooleanType),
            th.Property("communitiesEnabled", th.BooleanType),
            th.Property("contactsEnabled", th.BooleanType),
            th.Property("contentAiEnabled", th.BooleanType),
            th.Property("conversationsEnabled", th.BooleanType),
            th.Property("dashboardStatsEnabled", th.BooleanType),
            th.Property("exportPaymentsEnabled", th.BooleanType),
            th.Property("facebookAdsReportingEnabled", th.BooleanType),
            th.Property("funnelsEnabled", th.BooleanType),
            th.Property("invoiceEnabled", th.BooleanType),
            th.Property("leadValueEnabled", th.BooleanType),
            th.Property("marketingEnabled", th.BooleanType),
            th.Property("membershipEnabled", th.BooleanType),
            th.Property("onlineListingsEnabled", th.BooleanType),
            th.Property("opportunitiesEnabled", th.BooleanType),
            th.Property("paymentsEnabled", th.BooleanType),
            th.Property("phoneCallEnabled", th.BooleanType),
            th.Property("recordPaymentEnabled", th.BooleanType),
            th.Property("refundsEnabled", th.BooleanType),
            th.Property("reviewsEnabled", th.BooleanType),
            th.Property("settingsEnabled", th.BooleanType),
            th.Property("socialPlanner", th.BooleanType),
            th.Property("tagsEnabled", th.BooleanType),
            th.Property("triggersEnabled", th.BooleanType),
            th.Property("websitesEnabled", th.BooleanType),
            th.Property("workflowsEnabled", th.BooleanType),
            th.Property("workflowsReadOnly", th.BooleanType),
        )),
        th.Property("roles", th.ObjectType(
            th.Property("type", th.StringType),
            th.Property("role", th.StringType),
            th.Property("locationIds", th.ArrayType(th.StringType)),
        )),
        th.Property("deleted", th.BooleanType)
    ).to_dict()
