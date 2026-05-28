import os

import matplotlib.pyplot as plt
import pytest

from visualisation.graphs_core import GraphsCore


class TestPlotRs:
    def test_returns_figure(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_rs()
        assert isinstance(fig, plt.Figure)

    def test_has_two_subplots(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_rs()
        assert len(fig.axes) == 2

    def test_value_ax_has_two_lines(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_rs()
        assert len(fig.axes[0].lines) == 2

    def test_labels(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_rs()
        ax = fig.axes[0]
        assert ax.get_xlabel() == "Давление, атм"
        assert ax.get_ylabel() == "Rs, м³/м³"

    def test_saves_file(self, compare_core_rs_bo, pvt_data_rs_bo, tmp_path):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        path = str(tmp_path / "rs.png")
        graphs.plot_rs(save_path=path)
        assert os.path.exists(path)


class TestPlotBo:
    def test_returns_figure(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_bo()
        assert isinstance(fig, plt.Figure)

    def test_has_two_subplots(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_bo()
        assert len(fig.axes) == 2

    def test_value_ax_has_two_lines(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_bo()
        assert len(fig.axes[0].lines) == 2

    def test_labels(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_bo()
        ax = fig.axes[0]
        assert ax.get_xlabel() == "Давление, атм"
        assert ax.get_ylabel() == "Bo, м³/м³"

    def test_saves_file(self, compare_core_rs_bo, pvt_data_rs_bo, tmp_path):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        path = str(tmp_path / "bo.png")
        graphs.plot_bo(save_path=path)
        assert os.path.exists(path)


class TestPlotPb:
    def test_returns_figure(self, compare_core_pb, pvt_data_pb):
        graphs = GraphsCore(compare_core_pb, pvt_data_pb)
        fig = graphs.plot_pb()
        assert isinstance(fig, plt.Figure)

    def test_has_two_subplots(self, compare_core_pb, pvt_data_pb):
        graphs = GraphsCore(compare_core_pb, pvt_data_pb)
        fig = graphs.plot_pb()
        assert len(fig.axes) == 2

    def test_value_ax_has_two_lines(self, compare_core_pb, pvt_data_pb):
        graphs = GraphsCore(compare_core_pb, pvt_data_pb)
        fig = graphs.plot_pb()
        assert len(fig.axes[0].lines) == 2

    def test_labels(self, compare_core_pb, pvt_data_pb):
        graphs = GraphsCore(compare_core_pb, pvt_data_pb)
        fig = graphs.plot_pb()
        ax = fig.axes[0]
        assert ax.get_xlabel() == "Rsb, м³/м³"
        assert ax.get_ylabel() == "Pb, атм"

    def test_saves_file(self, compare_core_pb, pvt_data_pb, tmp_path):
        graphs = GraphsCore(compare_core_pb, pvt_data_pb)
        path = str(tmp_path / "pb.png")
        graphs.plot_pb(save_path=path)
        assert os.path.exists(path)


class TestPlotAll:
    def test_returns_figure(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_all()
        assert isinstance(fig, plt.Figure)

    def test_has_six_subplots(self, compare_core_rs_bo, pvt_data_rs_bo):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        fig = graphs.plot_all()
        assert len(fig.axes) == 6

    def test_saves_file(self, compare_core_rs_bo, pvt_data_rs_bo, tmp_path):
        graphs = GraphsCore(compare_core_rs_bo, pvt_data_rs_bo)
        path = str(tmp_path / "all.png")
        graphs.plot_all(save_path=path)
        assert os.path.exists(path)
