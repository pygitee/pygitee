# coding: utf-8

# flake8: noqa


from __future__ import absolute_import

# import models into model package
from gitee.models.blob import Blob
from gitee.models.body import Body
from gitee.models.body1 import Body1
from gitee.models.body10 import Body10
from gitee.models.body11 import Body11
from gitee.models.body12 import Body12
from gitee.models.body13 import Body13
from gitee.models.body14 import Body14
from gitee.models.body15 import Body15
from gitee.models.body16 import Body16
from gitee.models.body17 import Body17
from gitee.models.body18 import Body18
from gitee.models.body19 import Body19
from gitee.models.body2 import Body2
from gitee.models.body20 import Body20
from gitee.models.body21 import Body21
from gitee.models.body22 import Body22
from gitee.models.body23 import Body23
from gitee.models.body24 import Body24
from gitee.models.body25 import Body25
from gitee.models.body26 import Body26
from gitee.models.body27 import Body27
from gitee.models.body28 import Body28
from gitee.models.body29 import Body29
from gitee.models.body3 import Body3
from gitee.models.body30 import Body30
from gitee.models.body31 import Body31
from gitee.models.body32 import Body32
from gitee.models.body33 import Body33
from gitee.models.body34 import Body34
from gitee.models.body35 import Body35
from gitee.models.body36 import Body36
from gitee.models.body37 import Body37
from gitee.models.body38 import Body38
from gitee.models.body39 import Body39
from gitee.models.body4 import Body4
from gitee.models.body40 import Body40
from gitee.models.body41 import Body41
from gitee.models.body42 import Body42
from gitee.models.body43 import Body43
from gitee.models.body44 import Body44
from gitee.models.body45 import Body45
from gitee.models.body46 import Body46
from gitee.models.body47 import Body47
from gitee.models.body48 import Body48
from gitee.models.body49 import Body49
from gitee.models.body5 import Body5
from gitee.models.body50 import Body50
from gitee.models.body51 import Body51
from gitee.models.body52 import Body52
from gitee.models.body53 import Body53
from gitee.models.body54 import Body54
from gitee.models.body55 import Body55
from gitee.models.body56 import Body56
from gitee.models.body57 import Body57
from gitee.models.body58 import Body58
from gitee.models.body59 import Body59
from gitee.models.body6 import Body6
from gitee.models.body60 import Body60
from gitee.models.body61 import Body61
from gitee.models.body62 import Body62
from gitee.models.body63 import Body63
from gitee.models.body64 import Body64
from gitee.models.body65 import Body65
from gitee.models.body66 import Body66
from gitee.models.body67 import Body67
from gitee.models.body68 import Body68
from gitee.models.body69 import Body69
from gitee.models.body7 import Body7
from gitee.models.body70 import Body70
from gitee.models.body71 import Body71
from gitee.models.body72 import Body72
from gitee.models.body8 import Body8
from gitee.models.body9 import Body9
from gitee.models.branch import Branch
from gitee.models.code import Code
from gitee.models.code_comment import CodeComment
from gitee.models.code_forks import CodeForks
from gitee.models.code_forks_history import CodeForksHistory
from gitee.models.commit import Commit
from gitee.models.commit_content import CommitContent
from gitee.models.compare import Compare
from gitee.models.complete_branch import CompleteBranch
from gitee.models.content import Content
from gitee.models.content_basic import ContentBasic
from gitee.models.contributor import Contributor
from gitee.models.enterprise_basic import EnterpriseBasic
from gitee.models.enterprise_member import EnterpriseMember
from gitee.models.event import Event
from gitee.models.group import Group
from gitee.models.group_detail import GroupDetail
from gitee.models.group_followers import GroupFollowers
from gitee.models.group_member import GroupMember
from gitee.models.hook import Hook
from gitee.models.issue import Issue
from gitee.models.label import Label
from gitee.models.milestone import Milestone
from gitee.models.namespace import Namespace
from gitee.models.namespace_mini import NamespaceMini
from gitee.models.note import Note
from gitee.models.operate_log import OperateLog
from gitee.models.program_basic import ProgramBasic
from gitee.models.project import Project
from gitee.models.project_basic import ProjectBasic
from gitee.models.project_member import ProjectMember
from gitee.models.project_member_permission import ProjectMemberPermission
from gitee.models.project_stargazers import ProjectStargazers
from gitee.models.project_watchers import ProjectWatchers
from gitee.models.pull_request import PullRequest
from gitee.models.pull_request_comments import PullRequestComments
from gitee.models.pull_request_commits import PullRequestCommits
from gitee.models.pull_request_files import PullRequestFiles
from gitee.models.release import Release
from gitee.models.repo_commit import RepoCommit
from gitee.models.ssh_key import SSHKey
from gitee.models.ssh_key_basic import SSHKeyBasic
from gitee.models.tag import Tag
from gitee.models.tree import Tree
from gitee.models.user import User
from gitee.models.user_basic import UserBasic
from gitee.models.user_detail import UserDetail
from gitee.models.user_email import UserEmail
from gitee.models.user_info import UserInfo
from gitee.models.user_message import UserMessage
from gitee.models.user_message_list import UserMessageList
from gitee.models.user_mini import UserMini
from gitee.models.user_notification import UserNotification
from gitee.models.user_notification_count import UserNotificationCount
from gitee.models.user_notification_list import UserNotificationList
from gitee.models.user_notification_namespace import UserNotificationNamespace
from gitee.models.user_notification_subject import UserNotificationSubject
from gitee.models.week_report import WeekReport