from persistent import Persistent
from zope.container.contained import Contained
from zope.schema.fieldproperty import FieldProperty
from zc.datetimewidget.demo.interfaces import IDemoContent
from datetime import datetime
import zope.interface
import pytz


@zope.interface.implementer(IDemoContent)
class DemoContent(Persistent, Contained):

    startDate = FieldProperty(IDemoContent['startDate'])
    endDate = FieldProperty(IDemoContent['endDate'])

    startDatetime = FieldProperty(IDemoContent['startDatetime'])
    endDatetime = FieldProperty(IDemoContent['endDatetime'])

    severalDates = FieldProperty(IDemoContent['severalDates'])

    @property
    def now(self):
        return datetime.utcnow().replace(tzinfo=pytz.utc)
