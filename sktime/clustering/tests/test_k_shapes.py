# -*- coding: utf-8 -*-
"""Tests for time series k-shapes."""
import numpy as np
from sklearn import metrics

from sktime.clustering._k_shapes import TimeSeriesKShapes
from sktime.datasets import load_basic_motions

expected_results = [
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    2,
    2,
    1,
    2,
]

inertia = 0.550860917533926

expected_score = 0.6012820512820513

expected_iters = 4

expected_labels = [
    0,
    1,
    2,
    0,
    1,
    0,
    2,
    0,
    1,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
]


def test_kshapes():
    """Test implementation of Kshapes."""
    X_train, y_train = load_basic_motions(split="train")
    X_test, y_test = load_basic_motions(split="test")

    kshapes = TimeSeriesKShapes(random_state=1, n_clusters=3)
    kshapes.fit(X_train)
    test_shape_result = kshapes.predict(X_test)
    score = metrics.rand_score(y_test, test_shape_result)
    proba = kshapes.predict_proba(X_test)

    assert np.array_equal(test_shape_result, expected_results)
    assert score == expected_score
    assert kshapes.n_iter_ == expected_iters
    assert np.array_equal(kshapes.labels_, expected_labels)
    assert proba.shape == (40, 3)

    for val in proba:
        assert np.count_nonzero(val == 1.0) == 1
