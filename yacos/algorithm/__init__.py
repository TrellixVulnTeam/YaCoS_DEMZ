"""
Copyright 2021 Anderson Faustino da Silva.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .metaheuristics import SGA, PSO
from .random_ import Random
from .benchmark_reduction import BenchmarkReduction
from .sequence_reduction import SequenceReduction
from .best_k import BestK
from .batch_elimination import BatchElimination
from .iterative_elimination import IterativeElimination
from .combined_elimination import CombinedElimination
from .improved_batch_elimination import ImprovedBatchElimination
from .cbr import CBR
from .cbr_function import CBR_Function

__version__ = '1.0.0'
