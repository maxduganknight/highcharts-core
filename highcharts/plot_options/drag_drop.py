from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class DragHandle(HighchartsMeta):
    """Options for the drag handles available in column series."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._cursor = None
        self._line_color = None
        self._line_width = None
        self._path_formatter = None
        self._z_index = None

        self.class_name = kwargs.pop('class_name', 'highcharts-drag-handle')
        self.color = kwargs.pop('color', '#fff')
        self.cursor = kwargs.pop('cursor', None)
        self.line_color = kwargs.pop('line_color', 'rgba(0, 0, 0, 0.6)')
        self.line_width = kwargs.pop('line_width', 1)
        self.path_formatter = kwargs.pop('path_formatter', None)
        self.z_index = kwargs.pop('z_index', 901)

    @property
    def class_name(self) -> Optional[str]:
        """CSS class name of the guide box in this state. Defaults to
        ``'highcharts-drag-handle'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The fill color of the drag handles. Defaults to ``'#fff'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def cursor(self) -> Optional[str]:
        """The mouse cursor to use for the drag handles. By default (when
        :obj:`None <python:None>`), this intelligently switches between ``'ew-resize'``
        and ``'ns-resize'`` depending on the direction the point is being dragged.

        Acceptable values are:

          * ``'alias'``
          * ``'all-scroll'``
          * ``'auto'``
          * ``'cell'``
          * ``'col-resize'``
          * ``'context-menu'``
          * ``'copy'``
          * ``'crosshair'``
          * ``'default'``
          * ``'e-resize'``
          * ``'ew-resize'``
          * ``'grab'``
          * ``'grabbing'``
          * ``'help'``
          * ``'move'``
          * ``'n-resize'``
          * ``'ne-resize'``
          * ``'nesw-resize'``
          * ``'no-drop'``
          * ``'none'``
          * ``'not-allowed'``
          * ``'ns-resize'``
          * ``'nw-resize'``
          * ``'nwse-resize'``
          * ``'pointer'``
          * ``'progress'``
          * ``'row-resize'``
          * ``'s-resize'``
          * ``'se-resize'``
          * ``'sw-resize'``
          * ``'text'``
          * ``'vertical-text'``
          * ``'w-resize'``
          * ``'wait'``
          * ``'zoom-in'``
          * ``'zoom-out'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        if not value:
            self._cursor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.SUPPORTED_CURSOR_VALUES:
                raise errors.HighchartsValueError(f'cursor expects a valid cursor value. '
                                                  f'Received: {value}')
            self._cursor = value

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """The line color of the drag handles. Defaults to ``'rgba(0, 0, 0, 0.6)'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        if not value:
            self._line_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._line_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._line_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Gradient.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._line_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._line_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Pattern.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._line_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The line width for the drag handles. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def path_formatter(self) -> Optional[str]:
        """JavaScript function to define the SVG path to use for the drag handles. Takes
        the ``point`` as a (JavaScript) argument. Should return an SVG path in array
        format. The SVG path is automatically positioned on the point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._path_formatter

    @path_formatter.setter
    def path_formatter(self, value):
        self._path_formatter = validators.string(value, allow_empty = True)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """Drag handles' zIndex position. Defaults to ``901``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.pop('className', 'highcharts-drag-handle'),
            'color': as_dict.pop('color', '#fff'),
            'cursor': as_dict.pop('cursor', None),
            'line_color': as_dict.pop('lineColor', 'rgba(0, 0, 0, 0.6)'),
            'line_width': as_dict.pop('lineWidth', 1),
            'path_formatter': as_dict.pop('pathFormatter', None),
            'z_index': as_dict.pop('zIndex', 901)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'cursor': self.cursor,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'pathFormatter': self.path_formatter,
            'zIndex': self.z_index
        }

        return self.trim_dict(untrimmed)


class GuideBoxOptions(HighchartsMeta):
    """Style options for the guide box default state."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._cursor = None
        self._line_color = None
        self._line_width = None
        self._z_index = None

        self.class_name = kwargs.pop('class_name', 'highcharts-drag-box-default')
        self.color = kwargs.pop('color', 'rgba(0, 0, 0, 0.1)')
        self.cursor = kwargs.pop('cursor', 'move')
        self.line_color = kwargs.pop('line_color', '#888')
        self.line_width = kwargs.pop('line_width', 1)
        self.z_index = kwargs.pop('z_index', 900)

    @property
    def class_name(self) -> Optional[str]:
        """CSS class name of the guide box in this state. Defaults to
        ``'highcharts-drag-box-default'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Guide box fill color. Defaults to ``'rgba(0, 0, 0, 0.1)'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def cursor(self) -> Optional[str]:
        """The style of cursor to use when the user's mouse hovers over the data series.
        Defaults to ``'move'``.

        Acceptable values are:

          * ``'alias'``
          * ``'all-scroll'``
          * ``'auto'``
          * ``'cell'``
          * ``'col-resize'``
          * ``'context-menu'``
          * ``'copy'``
          * ``'crosshair'``
          * ``'default'``
          * ``'e-resize'``
          * ``'ew-resize'``
          * ``'grab'``
          * ``'grabbing'``
          * ``'help'``
          * ``'move'``
          * ``'n-resize'``
          * ``'ne-resize'``
          * ``'nesw-resize'``
          * ``'no-drop'``
          * ``'none'``
          * ``'not-allowed'``
          * ``'ns-resize'``
          * ``'nw-resize'``
          * ``'nwse-resize'``
          * ``'pointer'``
          * ``'progress'``
          * ``'row-resize'``
          * ``'s-resize'``
          * ``'se-resize'``
          * ``'sw-resize'``
          * ``'text'``
          * ``'vertical-text'``
          * ``'w-resize'``
          * ``'wait'``
          * ``'zoom-in'``
          * ``'zoom-out'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        if not value:
            self._cursor = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in constants.SUPPORTED_CURSOR_VALUES:
                raise errors.HighchartsValueError(f'cursor expects a valid cursor value. '
                                                  f'Received: {value}')
            self._cursor = value

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the border around the guide box. Defaults to ``'#888'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        if not value:
            self._line_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._line_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._line_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Gradient.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._line_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._line_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._line_color = Pattern.from_dict(value)
                else:
                    self._line_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._line_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the line around the guide box. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """Guide box zIndex position. Defaults to ``900``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.pop('className', 'highcharts-drag-box-default'),
            'color': as_dict.pop('color', 'rgba(0, 0, 0, 0.1)'),
            'cursor': as_dict.pop('cursor', 'move'),
            'line_color': as_dict.pop('lineColor', '#888'),
            'line_width': as_dict.pop('lineWidth', 1),
            'z_index': as_dict.pop('zIndex', 900)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'cursor': self.cursor,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'zIndex': self.z_index
        }

        return self.trim_dict(untrimmed)


class GuideBox(HighchartsMeta):
    """Style options for the guide box. The guide box has one state by default, the
    ``default`` state."""

    def __init__(self, **kwargs):
        self._default = None
        self.default = kwargs.pop('default', None)

    @property
    def default(self) -> Optional[GuideBoxOptions]:
        """Style options for the guide box default state.

        :rtype: :class:`GuideBoxOptions` or :obj:`None <python:None>`
        """
        return self._default

    @default.setter
    @class_sensitive(GuideBoxOptions)
    def default(self, value):
        self._default = value

    @classmethod
    def from_dict(cls, as_dict):
        return cls({
            'default': as_dict.pop('default', None)
        })

    def to_dict(self) -> dict:
        untrimmed = {
            'default': self.default
        }

        return self.trim_dict(untrimmed)


class DragDropOptions(HighchartsMeta):
    """The draggable-points module allows points to be moved around or modified in the
    chart.

    In addition to the options mentioned under the dragDrop API structure, the module
    fires three (JavaScript) events:

      * ``point.dragStart``
      * ``point.drag``
      * ``point.drop``

    """

    def __init__(self, **kwargs):
        self._draggable_x = None
        self._draggable_y = None
        self._drag_handle = None
        self._drag_max_x = None
        self._drag_max_y = None
        self._drag_min_x = None
        self._drag_min_y = None
        self._drag_precision_x = None
        self._drag_precision_y = None
        self._drag_sensitivity = 2
        self._group_by = None
        self._guide_box = None
        self._live_redraw = True

        self.draggable_x = kwargs.pop('draggable_x', None)
        self.draggable_y = kwargs.pop('draggable_y', None)
        self.drag_handle = kwargs.pop('drag_handle', None)
        self.drag_max_x = kwargs.pop('drag_max_x', None)
        self.drag_max_y = kwargs.pop('drag_max_y', None)
        self.drag_min_x = kwargs.pop('drag_min_x', None)
        self.drag_min_y = kwargs.pop('drag_min_y', None)
        self.drag_precision_x = kwargs.pop('drag_precision_x', None)
        self.drag_precision_y = kwargs.pop('drag_precision_y', None)
        self.drag_sensitivity = kwargs.pop('drag_sensitivity', 2)
        self.group_by = kwargs.pop('group_by', None)
        self.guide_box = kwargs.pop('guide_box', None)
        self.live_redraw = kwargs.pop('live_redraw', True)

    @property
    def draggable_x(self) -> Optional[bool]:
        """If ``True``, enables dragging along the X dimension. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_x

    @draggable_x.setter
    def draggable_x(self, value):
        if value is None:
            self._draggable_x = None
        else:
            self._draggable_x = bool(value)

    @property
    def draggable_y(self) -> Optional[bool]:
        """If ``True``, enables dragging along the Y dimension. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``False``.

        .. warning::

          This is not supported for TreeGrid axes (the default axis type in Gantt charts).

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_y

    @draggable_y.setter
    def draggable_y(self, value):
        if value is None:
            self._draggable_y = None
        else:
            self._draggable_y = bool(value)

    @property
    def drag_handle(self) -> Optional[DragHandle]:
        """Options for the drag handles available in column series.

        :rtype: :class:`DragHandle` or :obj:`None <python:None>`
        """
        return self._drag_handle

    @drag_handle.setter
    @class_sensitive(DragHandle)
    def drag_handle(self, value):
        self._drag_handle = value

    @property
    def drag_max_x(self) -> Optional[int | float | Decimal]:
        """The maximum X value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_max_x

    @drag_max_x.setter
    def drag_max_x(self, value):
        self._drag_max_x = validators.numeric(value, allow_empty = True)

    @property
    def drag_max_y(self) -> Optional[int | float | Decimal]:
        """The maximum Y value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_max_y

    @drag_max_y.setter
    def drag_max_y(self, value):
        self._drag_max_y = validators.numeric(value, allow_empty = True)

    @property
    def drag_min_x(self) -> Optional[int | float | Decimal]:
        """The minimum X value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_min_x

    @drag_min_x.setter
    def drag_min_x(self, value):
        self._drag_min_x = validators.numeric(value, allow_empty = True)

    @property
    def drag_min_y(self) -> Optional[int | float | Decimal]:
        """The minimum Y value the points can be moved to. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_min_y

    @drag_min_y.setter
    def drag_min_y(self, value):
        self._drag_min_y = validators.numeric(value, allow_empty = True)

    @property
    def drag_precision_x(self) -> Optional[int | float | Decimal]:
        """The X precision value to drag to for this series. Defaults to
        :obj:`None <python:None>`, which is equivalent to disabling for most axes except
        for category axes where the default is ``1``.

        Set to ``0`` to disable for all axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_precision_x

    @drag_precision_x.setter
    def drag_precision_x(self, value):
        self._drag_precision_x = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def drag_precision_y(self) -> Optional[int | float | Decimal]:
        """The Y precision value to drag to for this series. Defaults to
        :obj:`None <python:None>`, which is equivalent to disabling for most axes except
        for category axes where the default is ``1``.

        Set to ``0`` to disable for all axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_precision_y

    @drag_precision_y.setter
    def drag_precision_y(self, value):
        self._drag_precision_y = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def drag_sensitivity(self) -> Optional[int | float | Decimal]:
        """The number of pixels to drag the pointer before it counts as a drag operation.
        Defaults to ``2``.

        .. note::

          This prevents drag/drop to fire when just clicking or selecting points.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._drag_sensitivity

    @drag_sensitivity.setter
    def drag_sensitivity(self, value):
        self._drag_sensitivity = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def group_by(self) -> Optional[str]:
        """Group the points by a property. Points with the same property value will be
        grouped together when moving. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._group_by

    @group_by.setter
    def group_by(self, value):
        self._group_by = validators.string(value, allow_empty = True)

    @property
    def guide_box(self) -> Optional[GuideBox]:
        """Style options for the guide box. The guide box has one state by default, the
        ``default`` state.

        :rtype: :class:`GuideBox` or :obj:`None <python:None>`
        """
        return self._guide_box

    @guide_box.setter
    @class_sensitive(GuideBox)
    def guide_box(self, value):
        self._guide_box = value

    @property
    def live_redraw(self) -> Optional[bool]:
        """If ``True``, update points as they are dragged. If ``False``, a guide box is
        drawn to illustrate the new point size. Defaults to :obj:`None <python:None>`,
        which behaves as ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`.
        """
        return self._live_redraw

    @live_redraw.setter
    def live_redraw(self, value):
        if value is None:
            self._live_redraw = None
        else:
            self._live_redraw = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.pop('draggableX', None),
            'draggable_y': as_dict.pop('draggableY', None),
            'drag_handle': as_dict.pop('dragHandle', None),
            'drag_max_x': as_dict.pop('dragMaxX', None),
            'drag_max_y': as_dict.pop('dragMaxY', None),
            'drag_min_x': as_dict.pop('dragMinX', None),
            'drag_min_y': as_dict.pop('dragMinY', None),
            'drag_precision_x': as_dict.pop('dragPrecisionX', None),
            'drag_precision_y': as_dict.pop('dragPrecisionY', None),
            'drag_sensitivity': as_dict.pop('dragSensitivity', 2),
            'group_by': as_dict.pop('groupBy', None),
            'guide_box': as_dict.pop('guideBox', None),
            'live_redraw': as_dict.pop('liveRedraw', True)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw
        }

        return self.trim_dict(untrimmed)


class BoxPlotDragDropOptions(DragDropOptions):
    """The draggable-points module allows points to be moved around or modified in the
    chart."""

    def __init__(self, **kwargs):
        self._draggable_high = None
        self._draggable_low = None
        self._draggable_q1 = None
        self._draggable_q3 = None

        self.draggable_high = kwargs.pop('draggable_high', True)
        self.draggable_low = kwargs.pop('draggable_low', True)
        self.draggable_q1 = kwargs.pop('draggable_q1', True)
        self.draggable_q3 = kwargs.pop('draggable_q3', True)

        super(self).__init__(**kwargs)

    @property
    def draggable_high(self) -> Optional[bool]:
        """If ``True``, enables high value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_high

    @draggable_high.setter
    def draggable_high(self, value):
        if value is None:
            self._draggable_high = None
        else:
            self._draggable_high = bool(value)

    @property
    def draggable_low(self) -> Optional[bool]:
        """If ``True``, enables the low value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_low

    @draggable_low.setter
    def draggable_low(self, value):
        if value is None:
            self._draggable_low = None
        else:
            self._draggable_low = bool(value)

    @property
    def draggable_q1(self) -> Optional[bool]:
        """If ``True``, enables the Q1 value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_q1

    @draggable_q1.setter
    def draggable_q1(self, value):
        if value is None:
            self._draggable_q1 = None
        else:
            self._draggable_q1 = bool(value)

    @property
    def draggable_q3(self) -> Optional[bool]:
        """If ``True``, enables the Q3 value to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_q3

    @draggable_q3.setter
    def draggable_q3(self, value):
        if value is None:
            self._draggable_q3 = None
        else:
            self._draggable_q3 = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.pop('draggableX', None),
            'draggable_y': as_dict.pop('draggableY', None),
            'drag_handle': as_dict.pop('dragHandle', None),
            'drag_max_x': as_dict.pop('dragMaxX', None),
            'drag_max_y': as_dict.pop('dragMaxY', None),
            'drag_min_x': as_dict.pop('dragMinX', None),
            'drag_min_y': as_dict.pop('dragMinY', None),
            'drag_precision_x': as_dict.pop('dragPrecisionX', None),
            'drag_precision_y': as_dict.pop('dragPrecisionY', None),
            'drag_sensitivity': as_dict.pop('dragSensitivity', 2),
            'group_by': as_dict.pop('groupBy', None),
            'guide_box': as_dict.pop('guideBox', None),
            'live_redraw': as_dict.pop('liveRedraw', True),

            'draggable_high': as_dict.pop('draggableHigh', True),
            'draggable_low': as_dict.pop('draggableLow', True),
            'draggable_q1': as_dict.pop('draggableQ1', True),
            'draggable_q3': as_dict.pop('draggableQ3', True)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw,

            'draggableHigh': self.draggable_high,
            'draggableLow': self.draggable_low,
            'draggableQ1': self.draggable_q1,
            'draggableQ3': self.draggable_q3
        }

        return self.trim_dict(untrimmed)


class BulletDragDropOptions(DragDropOptions):
    """The draggable-points module allows points to be moved around or modified in the
    chart."""

    def __init__(self, **kwargs):
        self._draggable_target = None

        self.draggable_target = kwargs.pop('draggable_target', True)

        super(self).__init__(**kwargs)

    @property
    def draggable_target(self) -> Optional[bool]:
        """If ``True``, enables the target to be dragged individually. Defaults to
        :obj:`None <python:None>`, which is equivalent to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._draggable_target

    @draggable_target.setter
    def draggable_target(self, value):
        if value is None:
            self._draggable_target = None
        else:
            self._draggable_target = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'draggable_x': as_dict.pop('draggableX', None),
            'draggable_y': as_dict.pop('draggableY', None),
            'drag_handle': as_dict.pop('dragHandle', None),
            'drag_max_x': as_dict.pop('dragMaxX', None),
            'drag_max_y': as_dict.pop('dragMaxY', None),
            'drag_min_x': as_dict.pop('dragMinX', None),
            'drag_min_y': as_dict.pop('dragMinY', None),
            'drag_precision_x': as_dict.pop('dragPrecisionX', None),
            'drag_precision_y': as_dict.pop('dragPrecisionY', None),
            'drag_sensitivity': as_dict.pop('dragSensitivity', 2),
            'group_by': as_dict.pop('groupBy', None),
            'guide_box': as_dict.pop('guideBox', None),
            'live_redraw': as_dict.pop('liveRedraw', True),

            'draggable_target': as_dict.pop('draggableTarget', True)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'draggableX': self.draggable_x,
            'draggableY': self.draggable_y,
            'dragHandle': self.drag_handle,
            'dragMaxX': self.drag_max_x,
            'dragMaxY': self.drag_max_y,
            'dragMinX': self.drag_min_x,
            'dragMinY': self.drag_min_y,
            'dragPrecisionX': self.drag_precision_x,
            'dragPrecisionY': self.drag_precision_y,
            'dragSensitivity': self.drag_sensitivity,
            'groupBy': self.group_by,
            'guideBox': self.guide_box,
            'liveRedraw': self.live_redraw,

            'draggableTarget': self.draggable_target
        }

        return self.trim_dict(untrimmed)