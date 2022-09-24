ref > https://dara-blog.com/conect-ssh-gcp

1. local
	`ssh-keygen`
	1. ssh key
		`ls ~/.ssh` or `ls /User/yasebehiroto/.ssh`
		- `id_rsa` 秘密鍵
		- `id_rsa.pub` 公開鍵
		
		`cat ~/.ssh/id_rsa.pub`

1. GCP
	インスタンスの詳細＞編集
	sshに登録
	or https://console.cloud.google.com/compute/metadata/sshKeys


1. local
	`ssh -i ~/.ssh/id_rsa yasebehiroto@\{GCP外部IP\}`

1. GCP local
	ssh登録？
	`eval \` ssh-agent \` `
	`ssh-add`
