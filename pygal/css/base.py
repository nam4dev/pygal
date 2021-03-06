# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2018 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.

"""Base styles"""

CSS = """/*
 * This file is part of pygal
 *
 * A python svg graph plotting library
 * Copyright © 2012 Kozea

 * This library is free software: you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation, either version 3 of the License, or (at your option) any
 * later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with pygal. If not, see <http://www.gnu.org/licenses/>.
*/

/*
 * Font-sizes from config, override with care
 */

{{ id }} {
  -webkit-user-select: none;
  -webkit-font-smoothing: antialiased;
  font-family: {{ style.font_family }};
}

{{ id }}.title {
  font-family: {{ style.title_font_family }};
  font-size: {{ style.title_font_size }}px;
}

{{ id }}.legends .legend text {
  font-family: {{ style.legend_font_family }};
  font-size: {{ style.legend_font_size }}px;
}

{{ id }}.axis text {
  font-family: {{ style.label_font_family }};
  font-size: {{ style.label_font_size }}px;
}

{{ id }}.axis text.major {
  font-family: {{ style.major_label_font_family }};
  font-size: {{ style.major_label_font_size }}px;
}

{{ id }}.text-overlay text.value {
  font-family: {{ style.value_font_family }};
  font-size: {{ style.value_font_size }}px;
}

{{ id }}.text-overlay text.label {
  font-family: {{ style.value_label_font_family }};
  font-size: {{ style.value_label_font_size }}px;
}

{{ id }}.tooltip {
  font-family: {{ style.tooltip_font_family }};
  font-size: {{ style.tooltip_font_size }}px;
}

{{ id }}text.no_data {
  font-family: {{ style.no_data_font_family }};
  font-size: {{ style.no_data_font_size }}px;
}
"""
