from typing import Optional

from validator_collection import validators

from highcharts.series.base import SeriesBase
from highcharts.plot_options.pareto import ParetoOptions
from highcharts.utility_functions import mro_init, mro_to_dict


class ParetoSeries(SeriesBase, ParetoOptions):
    """Options to configure a Pareto series.

    A pareto diagram is a type of chart that contains both bars and a line graph,
    where individual values are represented in descending order by bars, and the
    cumulative total is represented by the line.

    .. figure:: _static/pareto-example.png
      :alt: Pareto Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._base_series = None

        self.base_series = kwargs.pop('base_series', None)

        mro_init(self, kwargs)

    @property
    def base_series(self) -> Optional[int | str]:
        """An integer identifying the index to use for the base series, or a string
        representing the id of the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._base_series

    @base_series.setter
    def base_series(self, value):
        if value is None:
            self._base_series = None
        else:
            try:
                value = validators.string(value)
            except ValueError:
                value = validators.integer(value)

            self._base_series = value

    @property
    def data(self) -> None:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All Pareto Series by definition return :obj:`None <python:None>` for their
          data. They are a special series, drawn in relationship to the
          :meth:`base_series <ParetoSeries.base_series>` specified, and do not receive
          independent data points of their own.

        :rtype: :obj:`None <python:None>`
        """
        return None

    @data.setter
    def data(self, value):
        pass

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'data': as_dict.pop('data', None),
            'id': as_dict.pop('id', None),
            'index': as_dict.pop('index', None),
            'legend_index': as_dict.pop('legendIndex', None),
            'name': as_dict.pop('name', None),
            'stack': as_dict.pop('stack', None),
            'x_axis': as_dict.pop('xAxis', None),
            'y_axis': as_dict.pop('yAxis', None),
            'z_index': as_dict.pop('zIndex', None),

            'base_series': as_dict.pop('baseSeries', None),
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'baseSeries': self.base_series
        }
        parent_as_dict = mro_to_dict(self) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)