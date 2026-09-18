# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A FastAPI app for tracking student attendance at a dance school. Very early stage: only student and dance-class CRUD-ish endpoints exist so far; attendance tracking itself is not yet implemented.

## Setup & running

```
uv venv
source .venv/bin/activate
uv run fastapi dev src/main.py
```

There is no lockfile/pyproject.toml — dependencies are declared only in `requirements.txt` (currently just `fastapi[standard]`).

There are no lint or test commands configured yet (no test suite, no linter config).

## Architecture

Layered structure under `src/`, with `src/main.py` as the FastAPI entrypoint that mounts routers:

- `controller/` — FastAPI `APIRouter`s. Each controller module owns its own in-memory list (e.g. `dance_classes = []` in `dance_class_controller.py`, `students = []` in `student_controller.py`) and a `get_*_service()` factory passed via `Depends()`. This means all data is process-local and reset on every server restart — there is no database wired up yet.
- `service/` — business logic, constructed with the in-memory list from the controller. Handles ID generation (`uuid.uuid4()`) and validation before appending to the list.
- `dto/` — pydantic models, split into a `*Create` input model (no `id`) and a full model (with `id`), e.g. `StudentCreate`/`Student`, `DanceClassCreate`/`DanceClassCreate`.
- `repository/` — currently a placeholder package (empty `__init__.py`, untracked). Intended to eventually replace the in-memory lists held by the controllers.

Module imports are root-relative (`from dto.student_dto import ...`, `from service.student_service import ...`), not package-relative — this only works because `src/` is the working directory `fastapi dev` runs from.

When adding a new domain entity, follow the existing student/dance-class pattern: a DTO pair in `dto/`, a service in `service/` taking an injected collection, and a controller in `controller/` owning that collection and exposing it via a `Depends()` factory.
