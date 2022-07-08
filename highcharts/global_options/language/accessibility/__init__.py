from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.global_options.language.accessibility.announce_new_data import AnnounceNewDataLanguageOptions
from highcharts.global_options.language.accessibility.axis import AxisLanguageOptions
from highcharts.global_options.language.accessibility.chart_types import ChartTypesLanguageOptions
from highcharts.global_options.language.accessibility.exporting import ExportingLanguageOptions
from highcharts.global_options.language.accessibility.legend import LegendLanguageOptions
from highcharts.global_options.language.accessibility.range_selector import RangeSelectorLanguageOptions
from highcharts.global_options.language.accessibility.screen_reader_section import ScreenReaderSectionLanguageOptions
from highcharts.global_options.language.accessibility.series import SeriesLanguageOptions, SeriesTypeDescriptions
from highcharts.global_options.language.accessibility.sonification import SonificationLanguageOptions
from highcharts.global_options.language.accessibility.table import TableLanguageOptions
from highcharts.global_options.language.accessibility.zoom import ZoomLanguageOptions


class AccessibilityLanguageOptions(HighchartsMeta):
    """Configuration of accessibility strings in the chart.

    .. note::

      Requires the
      `accessibility module <https://code.highcharts.com/modules/accessibility.js>`_
      to be loaded.

      For a description of the module and information on its features, see
      `Accessibility <https://www.highcharts.com/docs/chart-concepts/accessibility>`_.

    """

    def __init__(self, **kwargs):
        self._announce_new_data = None
        self._axis = None
        self._chart_container_label = None
        self._chart_types = None
        self._credits = None
        self._default_chart_title = None
        self._drillup_button = None
        self._exporting = None
        self._graphic_container_label = None
        self._legend = None
        self._range_selector = None
        self._screen_reader_section = None
        self._series = None
        self._series_type_descriptions = None
        self._sonification = None
        self._svg_container_label = None
        self._svg_container_title = None
        self._table = None
        self._thousands_separator = None
        self._zoom = None

        self.announce_new_data = kwargs.pop('announce_new_data', None)
        self.axis = kwargs.pop('axis', None)
        self.chart_container_label = kwargs.pop('chart_container_label',
                                                constants.DEFAULT_LANG_ACCESSIBILITY_CHART_CONTAINER_LABEL)
        self.chart_types = kwargs.pop('chart_types', None)
        self.credits = kwargs.pop('credits', constants.DEFAULT_LANG_ACCESSIBILITY_CREDITS)
        self.default_chart_title = kwargs.pop('default_chart_title',
                                              constants.DEFAULT_LANG_ACCESSIBILITY_DEFAULT_CHART_TITLE)
        self.drillup_button = kwargs.pop('drillup_button',
                                         constants.DEFAULT_LANG_ACCESSIBILITY_DRILLUP_BUTTON)
        self.exporting = kwargs.pop('exporting', None)
        self.graphic_container_label = kwargs.pop('graphic_container_label',
                                                  constants.DEFAULT_LANG_ACCESSIBILITY_GRAPHIC_CONTAINER_LABEL)
        self.legend = kwargs.pop('legend', None)
        self.range_selector = kwargs.pop('range_selector', None)
        self.screen_reader_section = kwargs.pop('screen_reader_section', None)
        self.series = kwargs.pop('series', None)
        self.series_type_description = kwargs.pop('series_type_description', None)
        self.sonification = kwargs.pop('sonification', None)
        self.svg_container_label = kwargs.pop('svg_container_label',
                                              constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_LABEL)
        self.svg_container_title = kwargs.pop('svg_container_title',
                                              constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_TITLE)
        self.table = kwargs.pop('table', None)
        self.thousands_separator = kwargs.pop('thousands_separator',
                                              constants.DEFAULT_LANG_ACCESSIBILITY_THOUSANDSSEP)
        self.zoom = kwargs.pop('zoom', None)

    @property
    def announce_new_data(self) -> Optional[AnnounceNewDataLanguageOptions]:
        """Default announcement for new data in charts.

        .. note::

          If (JavaScript) ``addPoint()`` or ``addSeries()`` is used, and only one
          series/point is added, the
          :meth:`AnnounceNewDataLanguageOptions.new_point_announce` and
          :meth:`AnnounceNewdata.new_series_announce` strings are used.

          The ``...single`` versions will be used if there is only one chart on the page,
          and the ``...multiple`` versions will be used if there are multiple charts on the
          page. For all other new data events, the
          :meth:`AnnounceNewData.new_data_announce` string will be used.

        :rtype: :class:`AnnounceNewDataLanguageOptions` or :obj:`None <python:None>`
        """
        return self._announce_new_data

    @announce_new_data.setter
    @class_sensitive(AnnounceNewDataLanguageOptions)
    def announce_new_data(self, value):
        self._announce_new_data = value

    @property
    def axis(self) -> Optional[AxisLanguageOptions]:
        """Axis description strings.

        :rtype: :class:`AxisLanguageOptions` or :obj:`None <python:None>`
        """
        return self._axis

    @axis.setter
    @class_sensitive(AxisLanguageOptions)
    def axis(self, value):
        self._axis = value

    @property
    def chart_container_label(self) -> str:
        f"""Label applied to the chart container. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_CHART_CONTAINER_LABEL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._chart_container_label

    @chart_container_label.setter
    def chart_container_label(self, value):
        self._chart_container_label = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_CHART_CONTAINER_LABEL

    @property
    def chart_types(self) -> Optional[ChartTypesLanguageOptions]:
        """Chart type description strings.

        .. note::

          This is added to the chart information region.

          If there is only a single series type used in the chart, we use the format
          string for the series type, or default if missing. There is one format string
          for cases where there is only a single series in the chart, and one for multiple
          series of the same type.

        :rtype: :class:`ChartTypesLanguageOptions` or :obj:`None <python:None>`
        """
        return self._chart_types

    @chart_types.setter
    @class_sensitive(ChartTypesLanguageOptions)
    def chart_types(self, value):
        self._chart_types = value

    @property
    def credits(self) -> str:
        f"""Content of the credits section. Defaults to:
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_CREDITS}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_CREDITS

    @property
    def default_chart_title(self) -> str:
        """The default title applied ot the chart. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_DEFAULT_CHART_TITLE}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._default_chart_title

    @default_chart_title.setter
    def default_chart_title(self, value):
        self._default_chart_title = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_DEFAULT_CHART_TITLE

    @property
    def drillup_button(self) -> str:
        f"""String for the drill-up button. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_DRILLUP_BUTTON}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._drillup_button

    @drillup_button.setter
    def drillup_button(self, value):
        self._drillup_button = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_DRILLUP_BUTTON

    @property
    def exporting(self) -> Optional[ExportingLanguageOptions]:
        """Exporting menu format strings for use in the accessibility module.

        :rtype: :class:`ExportingLanguageOptions` or :obj:`None <python:None>`
        """
        return self._exporting

    @exporting.setter
    @class_sensitive(ExportingLanguageOptions)
    def exporting(self, value):
        self._exporting = value

    @property
    def graphic_container_label(self) -> str:
        f"""Set a label on the container wrapping the SVG. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_GRAPHIC_CONTAINER_LABEL}'`` (an empty
        string).

        :rtype: :class:`str <python:str>`
        """
        return self._graphic_container_label

    @graphic_container_label.setter
    def graphic_container_label(self, value):
        self._graphic_container_label = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_GRAPHIC_CONTAINER_LABEL

    @property
    def legend(self) -> Optional[LegendLanguageOptions]:
        """Language options for the legend when used in accessibility mode.

        :rtype: :class:`LegendLanguageOptions` or :obj:`None <python:None>`
        """
        return self._legend

    @legend.setter
    @class_sensitive(LegendLanguageOptions)
    def legend(self, value):
        self._legend = value

    @property
    def range_selector(self) -> Optional[RangeSelectorLanguageOptions]:
        """Language options for range selectors when used in accessibility mode.

        :rtype: :class:`RangeSelectorLanguageOptions` or :obj:`None <python:None>`
        """
        return self._range_selector

    @range_selector.setter
    @class_sensitive(RangeSelectorLanguageOptions)
    def range_selector(self, value):
        self._range_selector = value

    @property
    def screen_reader_section(self) -> Optional[ScreenReaderSectionLanguageOptions]:
        """Language options for the screen reader information sections added before and
        after the chart when used in accessibility mode.

        :rtype: :class:`ScreenReaderSectionLanguageOptions` or :obj:`None <python:None>`
        """
        return self._screen_reader_section

    @screen_reader_section.setter
    @class_sensitive(ScreenReaderSectionLanguageOptions)
    def screen_reader_section(self, value):
        self._screen_reader_section = value

    @property
    def series(self) -> Optional[SeriesLanguageOptions]:
        """Language configuration for different series types.

        .. hint::

          For more dynamic control over the series element descriptions, see
          :meth:`Accessibility.series_description_formatter`.

        :rtype: :class:`SeriesLanguageOptions` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(SeriesLanguageOptions)
    def series(self, value):
        self._series = value

    @property
    def series_type_descriptions(self) -> Optional[SeriesTypeDescriptions]:
        """Descriptions of lesser known series types. The relevant description is added to
        the screen reader information region when these series types are used.

        :rtype: :class:`SeriesTypeDescriptions` or :obj:`None <python:None>`
        """
        return self._series_type_descriptions

    @series_type_descriptions.setter
    @class_sensitive(SeriesTypeDescriptions)
    def series_type_descriptions(self, value):
        self._series_type_descriptions = value

    @property
    def sonification(self) -> Optional[SonificationLanguageOptions]:
        """Language options for the sonification functionality when used in accessibility
        mode.

        :rtype: :class:`SonificationLanguageOptions` or :obj:`None <python:None>`
        """
        return self._sonification

    @sonification.setter
    @class_sensitive(SonificationLanguageOptions)
    def sonification(self, value):
        self._sonification = value

    @property
    def svg_container_label(self) -> str:
        f"""Set a label on the container wrapping the SVG. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_LABEL}'``.

        :rtype: :class:`str <python:str>`
        """
        return self._svg_container_label

    @svg_container_label.setter
    def svg_container_label(self, value):
        self._svg_container_label = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_LABEL

    @property
    def svg_container_title(self) -> str:
        f"""Title element text for the chart SVG element. Defaults to
        ``'{constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_TITLE}'`` (an empty
        string).

        .. note::

          Leave this empty to disable adding the title element. Browsers will display this
          content when hovering over elements in the chart. Assistive technology may use
          this element to label the chart.

        :rtype: :class:`str <python:str>`
        """
        return self._svg_container_title

    @svg_container_title.setter
    def svg_container_title(self, value):
        self._svg_container_title = validators.string(value, allow_empty = True) or \
            constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_TITLE

    @property
    def table(self) -> Optional[TableLanguageOptions]:
        """Language options for the table functionality when used in accessibility
        mode.

        :rtype: :class:`TableLanguageOptions` or :obj:`None <python:None>`
        """
        return self._table

    @table.setter
    @class_sensitive(TableLanguageOptions)
    def table(self, value):
        self._table = value

    @property
    def thousands_separator(self) -> str | constants.EnforcedNullType:
        f"""Thousands separator to use when formatting numbers for screen readers.
        Defaults to ``'{constants.DEFAULT_LANG_ACCESSIBILITY_THOUSANDSSEP}'``.

        Set to :obj:`None <python:None>` or to an :class:`EnforcedNullType` to use the
        separator defined in :meth:`Language.thousands_separator`.

        .. note::

          Note that many screen readers will not handle an empty space as a thousands
          separator, and will consider "11 700" as two numbers.

        :rtype: :class:`str <python:str>` or :class:`EnforcedNullType`
        """
        return self._thousands_separator

    @thousands_separator.setter
    def thousands_separator(self, value):
        if not value:
            self._thousands_separator = constants.EnforcedNull
        else:
            self._thousands_separator = validators.string(value, allow_empty = True)

    @property
    def zoom(self) -> Optional[ZoomLanguageOptions]:
        """Language options for the zoom functionality when used in accessibility
        mode.

        :rtype: :class:`ZoomLanguageOptions` or :obj:`None <python:None>`
        """
        return self._zoom

    @zoom.setter
    @class_sensitive(ZoomLanguageOptions)
    def zoom(self, value):
        self._zoom = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'announce_new_data': as_dict.pop('announceNewData', None),
            'axis': as_dict.pop('axis', None),
            'chart_container_label': as_dict.pop('chartContainerLabel',
                                                 constants.DEFAULT_LANG_ACCESSIBILITY_CHART_CONTAINER_LABEL),
            'chart_types': as_dict.pop('chartTypes', None),
            'credits': as_dict.pop('credits', constants.DEFAULT_LANG_ACCESSIBILITY_CREDITS),
            'default_chart_title': as_dict.pop('defaultChartTitle',
                                               constants.DEFAULT_LANG_ACCESSIBILITY_DEFAULT_CHART_TITLE),
            'drillup_button': as_dict.pop('drillUpButton',
                                          constants.DEFAULT_LANG_ACCESSIBILITY_DRILLUP_BUTTON),
            'exporting': as_dict.pop('exporting', None),
            'graphic_container_label': as_dict.pop('graphicContainerLabel',
                                                   constants.DEFAULT_LANG_ACCESSIBILITY_GRAPHIC_CONTAINER_LABEL),
            'legend': as_dict.pop('legend', None),
            'range_selector': as_dict.pop('rangeSelector', None),
            'screen_reader_section': as_dict.pop('screenReaderSection', None),
            'series': as_dict.pop('series', None),
            'series_type_description': as_dict.pop('seriesTypeDescription', None),
            'sonification': as_dict.pop('sonification', None),
            'svg_container_label': as_dict.pop('svgContainerLabel',
                                               constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_LABEL),
            'svg_container_title': as_dict.pop('svgContainerTitle',
                                               constants.DEFAULT_LANG_ACCESSIBILITY_SVG_CONTAINER_TITLE),
            'table': as_dict.pop('table', None),
            'thousands_separator': as_dict.pop('thousandsSep',
                                               constants.DEFAULT_LANG_ACCESSIBILITY_THOUSANDSSEP),
            'zoom': as_dict.pop('zoom', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'announceNewData': self.announce_new_data,
            'axis': self.axis,
            'chartContainerLabel': self.chart_container_label,
            'chartTypes': self.chart_types,
            'credits': self.credits,
            'defaultChartTitle': self.default_chart_title,
            'drillupButton': self.drillup_button,
            'exporting': self.exporting,
            'graphicContainerLabel': self.graphic_container_label,
            'legend': self.legend,
            'rangeSelector': self.range_selector,
            'screenReaderSection': self.screen_reader_section,
            'series': self.series,
            'seriesTypeDescription': self.series_type_description,
            'sonification': self.sonification,
            'svgContainerLabel': self.svg_container_label,
            'svgContainerTitle': self.svg_container_title,
            'table': self.table,
            'thousandsSep': self.thousands_separator,
            'zoom': self.zoom
        }

        return self.trim_dict(untrimmed)
