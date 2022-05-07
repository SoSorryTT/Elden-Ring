# Elden-Ring
Application for represent weapon that user can used in Elden Ring.

## Database
Example of the data in this project.

**Character Table**
| ID | CharacterID | Gender | Str | Dex | Int | Fai | Arc | Weight |
|----|-------------|--------|-----|-----|-----|-----|-----|--------|
| 1 | Nikolia | Male | 69 | 87 | 9 | 93 | 97 | 33 |

**Weapon Table**
| ID | WeaponType | WeaponName | Str | Dex | Int | Fai | Arc | WeaponWeight | WeaponSkill |
|----|------------|------------|-----|-----|-----|-----|-----|--------------|-------------|
| 1 | Straight Sword | Short Sword | 8 | 10 | 0 | 0 | 0 | 3 | Kick |

## Getting Started
| Name | Version |
|------|---------|
| Python | 3.8 or higher |
| SQLite3 CLI | 3.33.0 or higher |

### Install Package
1. Clone this project repository to your local computer.
    ```cmd
    git clone https://github.com/SoSorryTT/Elden-Ring.git
    ```

2. Get into the directory of this repository.
    ```cmd
    cd Elden-Ring
    ```

3. Create a virtual environment.
    ```cmd
    python3 -m venv venv
    ```

4. Activate the venv.
    ```cmd
    source venv/bin/activate
    ```

5. Install all required package.
    ```cmd
    pip3 install -r requirements.txt
    ```

6. Create your database.
    ```cmd
    sqlite3 sample.db < eldenring.schema
    ```

7. Import CSV data into database.
    ```cmd
    $ sqlite3 sample.db
    sqlite> .mode csv
    sqlite> .import data/character.csv character
    sqlite> .import data/weapon.csv weapon
    sqlite> .quit

## Project Diagram
![Eldenring_Diagram](https://user-images.githubusercontent.com/78094917/165695538-dc30ed6c-90db-4213-a8e8-005a8127aa75.jpg)

## Project Web API
![Eldenring_API](https://github.com/SoSorryTT/Elden-Ring.wiki.git)
