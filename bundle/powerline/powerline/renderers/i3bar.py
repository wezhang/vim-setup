# vim:fileencoding=utf-8:noet

from powerline.renderer import Renderer
import json


class I3barRenderer(Renderer):
	'''I3bar Segment Renderer.

	Currently works only for i3bgbar (i3 bar with custom patches).
	'''

	@staticmethod
	def hlstyle(*args, **kwargs):
		# We don't need to explicitly reset attributes, so skip those calls
		return ''

	def hl(self, contents, fg=None, bg=None, attr=None):
		segment = {
			"full_text": contents,
			"separator": False,
			"separator_block_width": 0,  # no seperators
		}

		if fg is not None:
			if fg is not False and fg[1] is not False:
				segment['color'] = "#{0:06x}".format(fg[1])
		if bg is not None:
			if bg is not False and bg[1] is not False:
				segment['background_color'] = "#{0:06x}".format(bg[1])
		# i3bar "pseudo json" requires one line at a time
		return json.dumps(segment) + ",\n"


renderer = I3barRenderer
