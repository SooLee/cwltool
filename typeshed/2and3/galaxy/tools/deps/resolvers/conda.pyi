# Stubs for galaxy.tools.deps.resolvers.conda (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ..resolvers import Dependency, DependencyResolver, InstallableDependencyResolver, ListableDependencyResolver, MappableDependencyResolver, MultipleDependencyResolver, SpecificationPatternDependencyResolver

DEFAULT_ENSURE_CHANNELS = ...  # type: str

class CondaDependencyResolver(DependencyResolver, MultipleDependencyResolver, ListableDependencyResolver, InstallableDependencyResolver, SpecificationPatternDependencyResolver, MappableDependencyResolver):
    dict_collection_visible_keys = ...  # type: Any
    resolver_type = ...  # type: str
    config_options = ...  # type: Any
    can_uninstall_dependencies = ...  # type: bool
    versionless = ...  # type: Any
    dependency_manager = ...  # type: Any
    conda_prefix_parent = ...  # type: Any
    ensure_channels = ...  # type: Any
    auto_init = ...  # type: Any
    conda_context = ...  # type: Any
    disabled = ...  # type: Any
    auto_install = ...  # type: Any
    copy_dependencies = ...  # type: Any
    def __init__(self, dependency_manager, **kwds) -> None: ...
    def clean(self, **kwds): ...
    def uninstall(self, requirements): ...
    def uninstall_environments(self, environments): ...
    def install_all(self, conda_targets): ...
    def resolve_all(self, requirements, **kwds): ...
    def merged_environment_name(self, conda_targets): ...
    def resolve(self, requirement, **kwds): ...
    def unused_dependency_paths(self, toolbox_requirements_status): ...
    def list_dependencies(self): ...
    def install_dependency(self, name, version, type, **kwds): ...
    @property
    def prefix(self): ...

class MergedCondaDependency(Dependency):
    dict_collection_visible_keys = ...  # type: Any
    dependency_type = ...  # type: str
    activate = ...  # type: Any
    conda_context = ...  # type: Any
    environment_path = ...  # type: Any
    cache_path = ...  # type: Any
    def __init__(self, conda_context, environment_path, exact, name: Optional[Any] = ..., version: Optional[Any] = ..., preserve_python_environment: bool = ...) -> None: ...
    @property
    def exact(self): ...
    @property
    def name(self): ...
    @property
    def version(self): ...
    def shell_commands(self, requirement): ...

class CondaDependency(Dependency):
    dict_collection_visible_keys = ...  # type: Any
    dependency_type = ...  # type: str
    cacheable = ...  # type: bool
    activate = ...  # type: Any
    conda_context = ...  # type: Any
    environment_path = ...  # type: Any
    cache_path = ...  # type: Any
    def __init__(self, conda_context, environment_path, exact, name: Optional[Any] = ..., version: Optional[Any] = ..., preserve_python_environment: bool = ...) -> None: ...
    @property
    def exact(self): ...
    @property
    def name(self): ...
    @property
    def version(self): ...
    def build_cache(self, cache_path): ...
    def set_cache_path(self, cache_path): ...
    def build_environment(self): ...
    def shell_commands(self, requirement): ...