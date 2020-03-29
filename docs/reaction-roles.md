---
description: Plugin to implement reaction based roles in server.
---

# Reaction Roles

## ;reaction

It contains multiple reaction based sub-commands.

```yaml
Aliases:
- reactions

Usage:
;reaction
```

### role

Manage reaction based roles throughout different channels. Reactions are added to specified messages.

```yaml
Aliases:
- roles

Usage:
;reaction role
```

#### add

Setup reaction roles over any custom message you wish or you may skip this parameter to let bot post

To use custom message, you can pass its shareable URL which can be obtained by right clicking over your custom

```yaml
Aliases:
- setup
- set

Usage:
'reaction role add [message] <roles...>
```

#### remove

Remove reaction roles from provided message.
To use custom message, you can pass its shareable URL which can be obtained by right clicking over your custom

```yaml
Aliases:
- delete

Usage:
;reaction role remove <message>
```
