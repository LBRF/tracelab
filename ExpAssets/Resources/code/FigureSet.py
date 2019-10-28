from os.path import exists, join

from klibs import P
from klibs.KLNamedObject import NamedObject
from klibs.KLUtilities import iterable
from klibs.KLGraphics import fill, blit, flip
from klibs.KLCommunication import message
from klibs.KLUserInterface import any_key


class FigureSet(NamedObject):

	def __init__(self, name):
		self.figures = []
		super(FigureSet, self).__init__(name)

	def __parse_values__(self):
		for v in self.figures:
			if iterable(v):
				self.figures.append(list(v))
			else:
				self.figures.append([v,1])

	def add_figure(self, figure_name):
		if iterable(figure_name):
			self.figures.append(list(figure_name))
		else:
			self.figures.append([figure_name, 1])

	def add_figures(self, *figures):
		for f in figures:
			self.add_figure(f)
