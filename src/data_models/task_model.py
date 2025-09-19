from pydantic import BaseModel
from typing import List, Optional


class Status(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    color: Optional[str] = None
    orderindex: Optional[int] = None
    type: Optional[str] = None


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    color: Optional[str] = None
    email: Optional[str] = None
    profilePicture: Optional[str] = None


class Watcher(User):
    initials: Optional[str] = None


class Sharing(BaseModel):
    public: Optional[bool] = None
    public_share_expires_on: Optional[str] = None
    public_fields: Optional[List[str]] = None
    token: Optional[str] = None
    seo_optimized: Optional[bool] = None


class ListModel(BaseModel):
    id: str
    name: Optional[str] = None
    access: Optional[bool] = None


class Project(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    hidden: Optional[bool] = None
    access: Optional[bool] = None


class Folder(Project):
    pass


class Space(BaseModel):
    id: Optional[str] = None


class Task(BaseModel):
    id: Optional[str] = None
    custom_id: Optional[str] = None
    custom_item_id: Optional[int] = None
    name: str
    text_content: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    orderindex: Optional[str] = None
    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    date_closed: Optional[str] = None
    date_done: Optional[str] = None
    archived: Optional[bool] = None
    creator: Optional[User] = None
    assignees: Optional[List[User]] = None
    group_assignees: Optional[List[User]] = None
    watchers: Optional[List[Watcher]] = None
    checklists: Optional[List] = None
    tags: Optional[List] = None
    parent: Optional[str] = None
    top_level_parent: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[str] = None
    start_date: Optional[str] = None
    points: Optional[str] = None
    time_estimate: Optional[str] = None
    time_spent: Optional[int] = None
    custom_fields: Optional[List] = None
    dependencies: Optional[List] = None
    linked_tasks: Optional[List] = None
    locations: Optional[List] = None
    team_id: Optional[str] = None
    url: Optional[str] = None
    sharing: Optional[Sharing] = None
    permission_level: Optional[str] = None
    list: Optional[ListModel] = None
    project: Optional[Project] = None
    folder: Optional[Folder] = None
    space: Optional[Space] = None






