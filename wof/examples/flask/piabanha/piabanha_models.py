from __future__ import (absolute_import, division, print_function)

from sqlalchemy import (Column, Integer, String, ForeignKey, Float, DateTime,
                        Boolean)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import wof.models as wof_base

Base = declarative_base()


def init_model(db_session):
    Base.query = db_session.query_property()

class Variable(Base, wof_base.BaseVariable):
    __tablename__ = 'variables'

    VariableID = Column('variableid', Integer, primary_key=True)
    VariableCode = Column('variablecode', String)
    VariableName = Column('variablename', String)
    VariableUnitsID = Column('variableunitsid', Integer, ForeignKey('units.unitsid'))
    SampleMedium = Column('samplemedium', String)
    ValueType = Column('valuetype', String)
    IsRegular = Column('isregular', Boolean)
    TimeSupport = Column('timesupport', Float)
    TimeUnitsID = Column('timeunitsid', Integer, ForeignKey('units.unitsid'))
    DataType = Column('datatype', String)
    GeneralCategory = Column('generalcategory', String)
    NoDataValue = Column('nodatavalue', Float)

    VariableUnits = relationship("Units",
                        primaryjoin='Variable.VariableUnitsID==Units.UnitsID')

    TimeUnits = relationship("Units",
                        primaryjoin='Variable.TimeUnitsID==Units.UnitsID')

    def __repr__(self):
        return "<Variable('%s','%s')>" % (self.VariableCode, self.VariableName)

class Site(Base, wof_base.BaseSite):
    __tablename__ = 'sites'

    SiteID = Column('siteid', Integer, primary_key = True)
    SiteCode = Column('sitecode', String)
    SiteName = Column('sitename', String)
    Latitude = Column('latitude', Float)
    Longitude = Column('longitude', Float)
    LatLongDatumID = Column('latlongdatumid', Integer,
                        ForeignKey('spatialreferences.spatialreferenceid')) #FK to SpatialReferences
    Elevation_m = Column('elevation_m', Float)
    VerticalDatum = Column('verticaldatum', String)
    LocalX = Column('localx', Float)
    LocalY = Column('localy', Float)
    LocalProjectionID = Column('localprojectionid', Integer,
                        ForeignKey('spatialreferences.spatialreferenceid')) #FK to SpatialReferences
    State = Column('state', String)
    County = Column('county', String)
    Comments = Column('comments', String)

    LatLongDatum = relationship("SpatialReference",
                                    primaryjoin='Site.LatLongDatumID==' +
                                        'SpatialReference.SpatialReferenceId')

    LocalProjection = relationship("SpatialReference",
                                    primaryjoin='Site.LocalProjectionID==' +
                                        'SpatialReference.SpatialReferenceId')

    def __repr__(self):
        return "<Site('%s','%s', ['%s' '%s'])>" % (self.SiteCode,
                                                   self.SiteName,
                                                   str(self.Latitude),
                                                   str(self.Longitude))

class DataValue(Base, wof_base.BaseDataValue):
    __tablename__ = 'datavalues'

    ValueID = Column('valueid', Integer, primary_key = True)
    DataValue = Column('datavalue', Float)
    ValueAccuracy = Column('valueaccuracy', Float)
    LocalDateTime = Column('localdatetime', DateTime)
    UTCOffset = Column('utcoffset', Float)
    DateTimeUTC = Column('datetimeutc', DateTime)
    SiteID = Column('siteid', Integer)
    VariableID = Column('variableid', Integer)
    OffsetValue = Column('offsetvalue', Float)
    OffsetTypeID = Column('offsettypeid', Integer)
    CensorCode = Column('censorcode', String)
    QualifierID = Column('qualifierid', Integer)
    MethodID = Column('methodid', Integer)
    SourceID = Column('sourceid', Integer)
    SampleID = Column('sampleid', Integer)
    QualityControlLevelID = Column('qualitycontrollevelid', Integer)

    @property
    def QualityControlLevel(self):
        for name_code in wof_base.QualityControlLevelTypes:
            if self.QualityControlLevelID==name_code[1]:
                return name_code[0]

        return wof_base.QualityControlLevelTypes['RAW_DATA'][0]

class Qualifier(Base, wof_base.BaseQualifier):
    __tablename__ = 'qualifiers'

    QualifierID = Column('qualifierid', Integer, primary_key=True)
    QualifierCode = Column('qualifiercode', String)
    QualifierDescription = Column('qualifierdescription', String)

class OffsetType(Base, wof_base.BaseOffsetType):
    __tablename__ = 'offsettypes'

    OffsetTypeID = Column('offsettypeid', Integer, primary_key = True)
    OffsetUnitsID = Column('offsetunitsid', Integer, ForeignKey('units.unitsid'))
    OffsetDescription = Column('offsetdescription', String)

    OffsetUnits = relationship("Units",
                primaryjoin='OffsetType.OffsetUnitsID==Units.UnitsID')


class Method(Base, wof_base.BaseMethod):
    __tablename__ = 'methods'

    MethodID = Column('methodid', Integer, primary_key=True)
    MethodDescription = Column('methoddescription', String)
    MethodLink = Column('methodlink', String)

class Source(Base, wof_base.BaseSource):
    __tablename__= 'sources'

    SourceID = Column('sourceid', Integer, primary_key=True)
    Organization = Column('organization', String)
    SourceDescription = Column('sourcedescription', String)
    SourceLink = Column('sourcelink', String)
    ContactName = Column('contactname', String)
    Phone = Column('phone', String)
    Email = Column('email', String)
    Address = Column('address', String)
    City = Column('city', String)
    State = Column('state', String)
    ZipCode = Column('zipcode', String)
    MetadataID = Column('metadataid', Integer, ForeignKey('isometadata.metadataid'))

    Metadata = relationship("Metadata",
                    primaryjoin='Source.MetadataID==Metadata.MetadataID')

class Metadata(Base, wof_base.BaseMetadata):
    __tablename__= 'isometadata'

    MetadataID = Column('metadataid', Integer, primary_key=True)
    TopicCategory = Column('topiccategory', String)
    Title = Column('title', String)
    Abstract = Column('abstract', String)
    ProfileVersion = Column('profileversion', String)
    MetadataLink = Column('metadatalink', String)

class QualityControlLevel(Base, wof_base.BaseQualityControlLevel):
    __tablename__= 'qualitycontrollevels'

    QualityControlLevelID = Column('qualitycontrollevelid', Integer, primary_key=True)
    QualityControlLevelCode = Column('qualitycontrollevelcode', String)

class Series(Base, wof_base.BaseSeries):
    __tablename__ = 'seriescatalog'

    SeriesID = Column('seriesid', Integer, primary_key = True)
    SiteID = Column('siteid', Integer, ForeignKey('sites.siteid'))
    SiteCode = Column('sitecode', String)
    SiteName = Column('sitename', String)
    VariableID = Column('variableid', Integer, ForeignKey('variables.variableid'))
    VariableCode = Column('variablecode', String)
    VariableName = Column('variablename', String)
    VariableUnitsID = Column('variableunitsid', Integer, ForeignKey('units.unitsid'))
    VariableUnitsName = Column('variableunitsname', String)
    SampleMedium = Column('samplemedium', String)
    ValueType = Column('valuetype', String)
    TimeSupport = Column('timesupport', Float)
    TimeUnitsID = Column('timeunitsid', Integer, ForeignKey('units.unitsid'))
    TimeUnitsName = Column('timeunitsname', String)
    DataType = Column('datatype', String)
    GeneralCategory = Column('generalcategory', String)
    MethodID = Column('methodid', Integer, ForeignKey('methods.methodid'))
    MethodDescription = Column('methoddescription', String)
    SourceID = Column('sourceid', Integer, ForeignKey('sources.sourceid'))
    Organization = Column('organization', String)
    SourceDescription = Column('sourcedescription', String)
    QualityControlLevelID = Column('qualitycontrollevelid', Integer) #TODO
    QualityControlLevelCode = Column('qualitycontrollevelcode', String)
    BeginDateTime = Column('begindatetime', DateTime)
    EndDateTime = Column('enddatetime', DateTime)
    BeginDateTimeUTC = Column('begindatetimeutc', DateTime)
    EndDateTimeUTC = Column('enddatetimeutc', DateTime)
    ValueCount = Column('valuecount', Integer)

    Site = relationship("Site",
                primaryjoin='Series.SiteID==Site.SiteID')

    Variable = relationship("Variable",
                primaryjoin='Series.VariableID==Variable.VariableID')

    Method = relationship("Method",
                primaryjoin='Series.MethodID==Method.MethodID')

    Source = relationship("Source",
                primaryjoin='Series.SourceID==Source.SourceID')


class Units(Base, wof_base.BaseUnits):
    __tablename__ = 'units'

    UnitsID = Column('unitsid', Integer, primary_key=True)
    UnitsName = Column('unitsname', String)
    UnitsType = Column('unitstype', String)
    UnitsAbbreviation = Column('unitsabbreviation', String)

class SpatialReference(Base, wof_base.BaseSpatialReference):
    __tablename__ = 'spatialreferences'

    SpatialReferenceId = Column('spatialreferenceid', Integer, primary_key=True)
    SRSID = Column('srsid', Integer)
    SRSName = Column('srsname', String)
    Notes = Column('notes', String)

class VerticalDatum(Base, wof_base.BaseVerticalDatum):
    __tablename__ = 'verticaldatumcv'
    Term = Column('term', String, primary_key=True)
    Definition = Column('definition', String)
