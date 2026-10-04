
from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

class labx(ABC):
    @staticmethod
    @abstractmethod
    def lab_1_problem_1(x, student_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def lab_1_problem_2(x, student_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def lab_1_problem_3(x, student_id):
        raise NotImplementedError

    @staticmethod
    def _phase(student_id):
        return (abs(int(student_id)) % 1000) / 1000.0 * np.pi

    @staticmethod
    def lab_1_problem_1(x, student_id):
        x = np.asarray(x, dtype=float)
        phase = labx._phase(student_id)
        return np.sin(x + phase) / (np.abs(x) + 1.0) + 0.5 * np.tanh(x / 3.0) + 1.0

    @staticmethod
    def lab_1_problem_2(x, student_id):
        x = np.asarray(x, dtype=float)
        phase = labx._phase(student_id)
        return np.exp(-0.08 * np.abs(x)) * (np.sin(x + phase) + 1.0)

    @staticmethod
    def lab_1_problem_3(x, student_id):
        x = np.asarray(x, dtype=float)
        phase = labx._phase(student_id)
        return np.cos(0.7 * x + phase) + 0.5 * np.sin(2.4 * x)

def lab_1_problem_1(x, student_id):
    return labx.lab_1_problem_1(x, student_id)

def lab_1_problem_2(x, student_id):
    return labx.lab_1_problem_2(x, student_id)

def lab_1_problem_3(x, student_id):
    return labx.lab_1_problem_3(x, student_id)

__all__ = ["labx", "lab_1_problem_1", "lab_1_problem_2", "lab_1_problem_3"]
