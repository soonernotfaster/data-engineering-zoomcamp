 #!/usr/bin/env bash

 docker run -it \
 -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
 -e PGADMIN_DEFAULT_PASSWORD="root" \
 -p 8080:80 \
 --network pg-network \
 --name pg-admin \
 dpage/pgadmin4
