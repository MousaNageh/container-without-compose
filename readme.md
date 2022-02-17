## steps to create connections bewteen containers without docker-compse file 

### 1) create a network (let's say mynet ): 
   - run the following command to create network 
   ```sh
   $ docker network create mynet
   ```
   - to check if the newwork is created run the following command : 
   ```sh
   $ docker network create mynet
   ```
### 2)create pull mysql image from docker hub :
   - to bull a mysql imges :
   ```sh
   $ docker pull mysql:5.7.37 
   ```
   - the run container : 
   ```sh
   $ docker run -d  --name  db -e MYSQL_ROOT_PASSWORD=root -v data:/var/lib/mysql  -d mysql:5.7.37  --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
   ```
   - tconnect to mysql: 
   ```sh
   $ docker exec -it db bash
   ```
   ```sh
   $ mysql -u root -p
   ```
   - the enter your password `root`
### 3) connect your database container and backend container to this network : 
   - add the container to the network by the following command 
   ```sh
   $ docker run [our_options] --network mynet image_name_or_id
   ```
## steps to create connections bewteen containers with docker-compse file 
- run the following to build  images and run containers 
   ```sh
   $ docker-compose up 
   ```
   or for detached mode
    ```sh
   $ docker-compose up -d
   ```
- stop and remove containers and network containers 
   ```sh
   $ docker-compose down
   ```
   to remove volumes as well 
    ```sh
   $ docker-compose down -v
   ```