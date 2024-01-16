<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティカリキュラム  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.HumanResources/blob/master/CurriculumVitae/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述**オープンな職務経歴書フォーマット**  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `aboutMe[object]`: 人物データ  	- `avatar[object]`: 画像、サムネイル、またはアバターを含むファイルへのリンクと代替説明文    
	- `birthday[date]`: 生年月日    
	- `contact[object]`: 特定の人と連絡を取る方法    
	- `description[string]`: 候補者の略歴    
	- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。    
	- `name[string]`: 候補者氏名    
	- `surnames[string]`: 姓 o 氏名    
	- `title[string]`: その人に関連する役割、関係、活動。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `careerPreferences`:   	- `contact[object]`: 特定の人と連絡を取る方法    
	- `goals[array]`: 会社のニーズや要件に合致した個人的・職業的目標。    
	- `preferences[object]`: 仕事を引き受ける候補者の希望    
	- `requirements`:     
	- `status`:     
- `currentSalary[object]`: 報復の記述のあるオブジェクト  	- `amount[integer]`: 給与額    
	- `currency[string]`: ISO 4217による通貨記号    
	- `relevantPerks`:     
- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `experience[object]`: 職業経験に関する項目  	- `jobs[array]`: あなたが給与を得るために働いている、または働いたことのある企業、公的機関、NGO、その他の組織のリスト    
	- `projects`:     
	- `publicArtifacts`:     
- `id[*]`: エンティティの一意識別子  - `interestingFacts[array]`: IDE、好きな本、サッカーチーム...。  - `knowledge`:   	- `languages`:     
- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `noticePeriod[number]`: 退職予告期間  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `recommendations[array]`: プロフェッショナルとしての私を定義するのに役立つ、私が好きで推薦するコンテンツ。  - `relevantLinks[array]`: 本人の関連リンク  - `relevantYearsOfExperience[number]`: 希望する職業上の役割や目標に関連する経験年数。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `settings[object]`: CV設定  	- `language[string]`: ISO639-1コード](https://en.wikipedia.org/wiki/ISO_639-1)で表されるCVの言語。    
	- `lastUpdate[date]`: 履歴書の最終更新日    
- `significativeRelationships[array]`: 一緒に仕事をしたことがあるかないかにかかわらず、私との関係が私をプロフェッショナルとして定義するのに役立つ友人や同僚。  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIデータ型。CurriculumVitaeでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
オリジナルの http://github.com/manfred/mac/schema.json の位置からマップされた位置は、SDM のほとんどの位置で置き換えられた。また、データモデルのさまざまな使用を可能にするために、必要な属性と制限のほとんどを削除した。住所と所在地はSDM（schema.org）に適合させた。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CurriculumVitae:    
  description: An open Curriculum vitae format    
  properties:    
    aboutMe:    
      description: A Person data    
      properties:    
        avatar:    
          description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
          properties:    
            alt:    
              description: Alternative description of the image    
              type: string    
            data:    
              description: The raw data of the image    
              type: string    
              x-ngsi:    
                type: Property    
            encoding:    
              description: The constant value base64 for encoding the images    
              enum:    
                - base64    
              type: string    
              x-ngsi:    
                type: Property    
            link:    
              description: 'Link to the stored image '    
              format: uri    
              type: string    
              x-ngsi:    
                type: Property    
            mediaType:    
              description: the media type of the image    
              enum:    
                - image/png    
                - image/jpeg    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        birthday:    
          description: Person's birth date    
          format: date    
          type: string    
        contact:    
          anyOf:    
            - publicProfiles:    
                description: Online services that provide a way to contact a person without exposing mail or phone number.    
                items:    
                  properties:    
                    URL:    
                      description: Link to the candidate's profiles    
                      format: uri    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    type:    
                      description: Public profiles in social networks or equivalent resources    
                      enum:    
                        - github    
                        - linkedin    
                        - manfred    
                        - other    
                        - stackoverflow    
                        - twitter    
                        - xing    
                        - website    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                type: array    
                x-ngsi:    
                  type: Property    
            - phoneNumbers:    
                description: Phone numbers to contact the candidate    
                items:    
                  properties:    
                    countryCode:    
                      description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    number:    
                      description: Phone number without the country prefix    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                type: array    
                x-ngsi:    
                  type: Property    
            - contactMails:    
                description: Contact emails of the candidate    
                items:    
                  description: Every contact email of the candidate    
                  format: email    
                  type: string    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
          description: A way to contact a specific person    
          type: object    
          x-ngsi:    
            type: Property    
        description:    
          description: Brief bio of the candidate    
          type: string    
          x-ngsi:    
            type: Property    
        location:    
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
          oneOf:    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type:    
                enum:    
                  - Point    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type:    
                enum:    
                  - LineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type:    
                enum:    
                  - Polygon    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPoint    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 2    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiLineString    
                type: string    
            - bbox:    
                items:    
                  type: number    
                minItems: 4    
                type: array    
              coordinates:    
                items:    
                  items:    
                    items:    
                      items:    
                        type: number    
                      minItems: 2    
                      type: array    
                    minItems: 4    
                    type: array    
                  type: array    
                type: array    
              type:    
                enum:    
                  - MultiPolygon    
                type: string    
          x-ngsi:    
            type: GeoProperty    
        name:    
          description: Name of the candidate    
          type: string    
          x-ngsi:    
            type: Property    
        surnames:    
          description: Surname o Surnames of the person    
          type: string    
        title:    
          description: 'Role, relationship or activity related to the person.'    
          type: string    
      type: object    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    careerPreferences:    
      properties:    
        contact:    
          anyOf:    
            - publicProfiles:    
                description: Online services that provide a way to contact a person without exposing mail or phone number.    
                items:    
                  properties:    
                    URL:    
                      description: Link to the candidate's profiles    
                      format: uri    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    type:    
                      description: Public profiles in social networks or equivalent resources    
                      enum:    
                        - github    
                        - linkedin    
                        - manfred    
                        - other    
                        - stackoverflow    
                        - twitter    
                        - xing    
                        - website    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                type: array    
                x-ngsi:    
                  type: Property    
            - phoneNumbers:    
                description: Phone numbers to contact the candidate    
                items:    
                  properties:    
                    countryCode:    
                      description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    number:    
                      description: Phone number without the country prefix    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                type: array    
                x-ngsi:    
                  type: Property    
            - contactMails:    
                description: Contact emails of the candidate    
                items:    
                  description: Every contact email of the candidate    
                  format: email    
                  type: string    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
          description: A way to contact a specific person    
          type: object    
          x-ngsi:    
            type: Property    
        goals:    
          description: Personal and Professional goals to match with company needs and requirements.    
          items:    
            description: Every Personal and Professional goals to match with company needs and requirements    
            properties:    
              description:    
                description: 'Long description of the goals like Learn German, Become Team Leader, Work in a Silicon Valley Company '    
                type: string    
                x-ngsi:    
                  type: Property    
              title:    
                description: 'Short description of the goals like Learn German, Become Team Leader, Work in a Silicon Valley Company'    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        preferences:    
          description: Preferences of the Candidate to accept the work    
          properties:    
            discardedCompetences:    
              description: 'Skills, tools, domains or methodologies I don''t like to work with'    
              items:    
                description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                properties:    
                  description:    
                    description: Description of the competence    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the competence    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: type of the competence    
                    enum:    
                      - domain    
                      - hardware    
                      - practice    
                      - technology    
                      - tool    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
              type: array    
              x-ngsi:    
                type: Property    
            discardedOrganizations:    
              description: Type of organizations where I don't want to work    
              items:    
                description: Types of Organization    
                enum:    
                  - academicalInstitution    
                  - bigCorp    
                  - freelance    
                  - NGO    
                  - other    
                  - publicAdministration    
                  - SME    
                  - startup    
                type: string    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            discardedRoles:    
              description: Type of roles I don't like to adopt    
              items:    
                description: 'Preferred roles like Project Manager, CIO, etc'    
                type: string    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            preferredCompetences:    
              description: 'Skills, tools, domains or methodologies I like to work with'    
              items:    
                description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                properties:    
                  description:    
                    description: Description of the competence    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the competence    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: type of the competence    
                    enum:    
                      - domain    
                      - hardware    
                      - practice    
                      - technology    
                      - tool    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
              type: array    
              x-ngsi:    
                type: Property    
            preferredOrganizations:    
              description: Type of organizations where I want to work    
              items:    
                description: Types of Organization    
                enum:    
                  - academicalInstitution    
                  - bigCorp    
                  - freelance    
                  - NGO    
                  - other    
                  - publicAdministration    
                  - SME    
                  - startup    
                type: string    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            preferredRoles:    
              description: 'Preferred roles like ''Product Manager'', ''Chef'', ''Teacher'''    
              items:    
                description: Every role description    
                type: string    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        requirements:    
          properties:    
            compensation:    
              properties:    
                equity:    
                  properties:    
                    comments:    
                      description: Comments about the equity percentage    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    from:    
                      description: Minimum percentage of equity    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    mustHave:    
                      description: If equity is a must have to accept a new position    
                      type: boolean    
                      x-ngsi:    
                        type: Property    
                    upto:    
                      description: Maximum percentage of equity    
                      type: number    
                      x-ngsi:    
                        type: Property    
                  type: object    
                perks:    
                  allOf:    
                    - mustHave:    
                        description: Perks a new position must have to be considered    
                        items:    
                          description: Mandatory requirements    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        type: array    
                        x-ngsi:    
                          type: Property    
                    - niceToHave:    
                        description: Perks a new position should have to be considered    
                        items:    
                          description: Items in retribution nice to have    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        type: array    
                        x-ngsi:    
                          type: Property    
                  description: Other non-monetary retribution    
                  type: object    
                  x-ngsi:    
                    type: Property    
                salary:    
                  properties:    
                    comments:    
                      description: Other comments on the salary    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    currency:    
                      description: in ISO 4217 currency format    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    from:    
                      description: Minimum salary accepted by the candidate    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    upto:    
                      description: Maximum salary accepted by the candidate    
                      type: number    
                      x-ngsi:    
                        type: Property    
                  type: object    
              type: object    
            contractTypes:    
              description: Type of contract with the entity / organization    
              items:    
                description: Types of Contracts    
                enum:    
                  - freelance    
                  - internship    
                  - permanent    
                  - temporary    
                type: string    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            situation:    
              description: Details about working location    
              properties:    
                comments:    
                  description: Other conditions or comments about the candidate    
                  type: string    
                  x-ngsi:    
                    type: Property    
                openToRelocate:    
                  description: 'Candidate accepts relocation '    
                  type: boolean    
                  x-ngsi:    
                    type: Property    
                openToRemote:    
                  description: 'Candidate accepts remote work '    
                  type: boolean    
                  x-ngsi:    
                    type: Property    
                remoteOnly:    
                  description: 'Candidate only accepts remote work '    
                  type: boolean    
                  x-ngsi:    
                    type: Property    
                workingAreas:    
                  description: 'Locations where the candidate accepts as working locations '    
                  items:    
                    properties:    
                      distanceFromMunicipality:    
                        description: Distance from municipality accepted by the candidate    
                        properties:    
                          amount:    
                            description: Number of miles / km    
                            type: integer    
                            x-ngsi:    
                              type: Property    
                          unit:    
                            description: 'Unit of measure, Kilometers or Miles'    
                            enum:    
                              - Km    
                              - Mi    
                            type: string    
                            x-ngsi:    
                              type: Property    
                        type: object    
                        x-ngsi:    
                          type: Property    
                      location:    
                        description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                        oneOf:    
                          - description: Geojson reference to the item. Point    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  type: number    
                                minItems: 2    
                                type: array    
                              type:    
                                enum:    
                                  - Point    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON Point    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                          - description: Geojson reference to the item. LineString    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  items:    
                                  minItems: 2    
                                  type: array    
                                minItems: 2    
                                type: array    
                              type:    
                                enum:    
                                  - LineString    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON LineString    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                          - description: Geojson reference to the item. Polygon    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  items:    
                                  minItems: 4    
                                  type: array    
                                type: array    
                              type:    
                                enum:    
                                  - Polygon    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON Polygon    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                          - description: Geojson reference to the item. MultiPoint    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  items:    
                                  minItems: 2    
                                  type: array    
                                type: array    
                              type:    
                                enum:    
                                  - MultiPoint    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON MultiPoint    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                          - description: Geojson reference to the item. MultiLineString    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  items:    
                                  minItems: 2    
                                  type: array    
                                type: array    
                              type:    
                                enum:    
                                  - MultiLineString    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON MultiLineString    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                          - description: Geojson reference to the item. MultiLineString    
                            properties:    
                              bbox:    
                                items:    
                                  type: number    
                                minItems: 4    
                                type: array    
                              coordinates:    
                                items:    
                                  items:    
                                  type: array    
                                type: array    
                              type:    
                                enum:    
                                  - MultiPolygon    
                                type: string    
                            required:    
                              - type    
                              - coordinates    
                            title: GeoJSON MultiPolygon    
                            type: object    
                            x-ngsi:    
                              type: GeoProperty    
                        x-ngsi:    
                          type: GeoProperty    
                    type: object    
                  type: array    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
        status:    
          enum:    
            - notAvailable    
            - openToOffers    
            - searchingActively    
          type: string    
      type: object    
    currentSalary:    
      description: Object with the description of the retribution    
      properties:    
        amount:    
          description: Monetary salary amount    
          type: integer    
          x-ngsi:    
            type: Property    
        currency:    
          description: Symbol of the currency using ISO 4217    
          type: string    
          x-ngsi:    
            type: Property    
        relevantPerks:    
          items:    
            description: Other non-monetary retributions    
            type: string    
            x-ngsi:    
              type: Property    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    experience:    
      description: Items describing the professional experience    
      properties:    
        jobs:    
          description: 'List of companies, Public Institutions, NGO or other organizations where you work or have worked for a salary.'    
          items:    
            description: 'Company, Public Institution, NGO or other organizations where you work or have worked for a salary.'    
            properties:    
              organization:    
                description: 'Organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                properties:    
                  URL:    
                    description: 'Link to the site of the Organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                    format: uri    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  address:    
                    description: The mailing address    
                    properties:    
                      addressCountry:    
                        description: 'The country. For example, Spain'    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/addressCountry    
                          type: Property    
                      addressLocality:    
                        description: 'The locality in which the street address is, and which is in the region'    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/addressLocality    
                          type: Property    
                      addressRegion:    
                        description: 'The region in which the locality is, and which is in the country'    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/addressRegion    
                          type: Property    
                      district:    
                        description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      postOfficeBoxNumber:    
                        description: 'The post office box number for PO box addresses. For example, 03578'    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/postOfficeBoxNumber    
                          type: Property    
                      postalCode:    
                        description: 'The postal code. For example, 24004'    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/https://schema.org/postalCode    
                          type: Property    
                      streetAddress:    
                        description: The street address    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/streetAddress    
                          type: Property    
                      streetNr:    
                        description: Number identifying a specific property on a public street    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      model: https://schema.org/address    
                      type: Property    
                  description:    
                    description: 'Description of the organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  image:    
                    description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                    properties:    
                      alt:    
                        description: Alternative description of the image    
                        type: string    
                      data:    
                        description: The raw data of the image    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      encoding:    
                        description: The constant value base64 for encoding the images    
                        enum:    
                          - base64    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      link:    
                        description: 'Link to the stored image '    
                        format: uri    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      mediaType:    
                        description: the media type of the image    
                        enum:    
                          - image/png    
                          - image/jpeg    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: 'Name of the organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              roles:    
                description: role played on the entity / organization    
                items:    
                  description: Roles developed within an organization    
                  properties:    
                    challenges:    
                      description: List of challenges faced while assuming the role    
                      items:    
                        properties:    
                          actions:    
                            description: Actions taken to solve the challenges while playing this role    
                            items:    
                              description: Every action taken to solve the challenges while playing this role    
                              type: string    
                              x-ngsi:    
                                type: Property    
                            type: array    
                            x-ngsi:    
                              type: Property    
                          description:    
                            description: Every challenge faced while assuming the role    
                            type: string    
                            x-ngsi:    
                              type: Property    
                        type: object    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    competences:    
                      items:    
                        description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                        properties:    
                          description:    
                            description: Description of the competence    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          name:    
                            description: Name of the competence    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          type:    
                            description: type of the competence    
                            enum:    
                              - domain    
                              - hardware    
                              - practice    
                              - technology    
                              - tool    
                            type: string    
                            x-ngsi:    
                              type: Property    
                        type: object    
                      type: array    
                    finishDate:    
                      description: End date of the role    
                      format: date    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    name:    
                      description: Name of the role    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    notes:    
                      description: Notes and information about the role    
                      type: string    
                    referrals:    
                      items:    
                        description: A Person data    
                        properties:    
                          avatar:    
                            description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                            properties:    
                              alt:    
                                description: Alternative description of the image    
                                type: string    
                              data:    
                                description: The raw data of the image    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              encoding:    
                                description: The constant value base64 for encoding the images    
                                enum:    
                                  - base64    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              link:    
                                description: 'Link to the stored image '    
                                format: uri    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              mediaType:    
                                description: the media type of the image    
                                enum:    
                                  - image/png    
                                  - image/jpeg    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                            type: object    
                            x-ngsi:    
                              type: Property    
                          birthday:    
                            description: Person's birth date    
                            format: date    
                            type: string    
                          contact:    
                            anyOf:    
                              - properties:    
                                  publicProfiles:    
                                    description: Online services that provide a way to contact a person without exposing mail or phone number.    
                                    items:    
                                      properties:    
                                        URL:    
                                          description: Link to the candidate's profiles    
                                          format: uri    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                        type:    
                                          description: Public profiles in social networks or equivalent resources    
                                          enum:    
                                            - github    
                                            - linkedin    
                                            - manfred    
                                            - other    
                                            - stackoverflow    
                                            - twitter    
                                            - xing    
                                            - website    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                      type: object    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                              - properties:    
                                  phoneNumbers:    
                                    description: Phone numbers to contact the candidate    
                                    items:    
                                      properties:    
                                        countryCode:    
                                          description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                                          type: number    
                                          x-ngsi:    
                                            type: Property    
                                        number:    
                                          description: Phone number without the country prefix    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                      type: object    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                              - properties:    
                                  contactMails:    
                                    description: Contact emails of the candidate    
                                    items:    
                                      description: Every contact email of the candidate    
                                      format: email    
                                      type: string    
                                      x-ngsi:    
                                        type: Property    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                            description: A way to contact a specific person    
                            type: object    
                            x-ngsi:    
                              type: Property    
                          description:    
                            description: Brief bio of the candidate    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          location:    
                            description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                            oneOf:    
                              - description: Geojson reference to the item. Point    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      type: number    
                                    minItems: 2    
                                    type: array    
                                  type:    
                                    enum:    
                                      - Point    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON Point    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. LineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    minItems: 2    
                                    type: array    
                                  type:    
                                    enum:    
                                      - LineString    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON LineString    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. Polygon    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 4    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - Polygon    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON Polygon    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiPoint    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiPoint    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiPoint    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiLineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiLineString    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiLineString    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiLineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiPolygon    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiPolygon    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                            x-ngsi:    
                              type: GeoProperty    
                          name:    
                            description: Name of the candidate    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          surnames:    
                            description: Surname o Surnames of the person    
                            type: string    
                          title:    
                            description: 'Role, relationship or activity related to the person.'    
                            type: string    
                        type: object    
                      type: array    
                    startDate:    
                      description: Start date of the role    
                      format: date    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
              type:    
                description: Types of Organization    
                enum:    
                  - academicalInstitution    
                  - bigCorp    
                  - freelance    
                  - NGO    
                  - other    
                  - publicAdministration    
                  - SME    
                  - startup    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        projects:    
          items:    
            properties:    
              details:    
                description: 'Organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                properties:    
                  URL:    
                    description: 'Link to the site of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    format: uri    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  description:    
                    description: 'Description of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  image:    
                    description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                    properties:    
                      alt:    
                        description: Alternative description of the image    
                        type: string    
                      data:    
                        description: The raw data of the image    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      encoding:    
                        description: The constant value base64 for encoding the images    
                        enum:    
                          - base64    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      link:    
                        description: 'Link to the stored image '    
                        format: uri    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      mediaType:    
                        description: the media type of the image    
                        enum:    
                          - image/png    
                          - image/jpeg    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  location:    
                    description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                    oneOf:    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - Point    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - LineString    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 4    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - Polygon    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPoint    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiLineString    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPolygon    
                          type: string    
                    x-ngsi:    
                      type: GeoProperty    
                  name:    
                    description: 'Name of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              roles:    
                items:    
                  description: Roles developed within an organization    
                  properties:    
                    challenges:    
                      description: List of challenges faced while assuming the role    
                      items:    
                        properties:    
                          actions:    
                            description: Actions taken to solve the challenges while playing this role    
                            items:    
                              description: Every action taken to solve the challenges while playing this role    
                              type: string    
                              x-ngsi:    
                                type: Property    
                            type: array    
                            x-ngsi:    
                              type: Property    
                          description:    
                            description: Every challenge faced while assuming the role    
                            type: string    
                            x-ngsi:    
                              type: Property    
                        type: object    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    competences:    
                      items:    
                        description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                        properties:    
                          description:    
                            description: Description of the competence    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          name:    
                            description: Name of the competence    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          type:    
                            description: type of the competence    
                            enum:    
                              - domain    
                              - hardware    
                              - practice    
                              - technology    
                              - tool    
                            type: string    
                            x-ngsi:    
                              type: Property    
                        type: object    
                      type: array    
                    finishDate:    
                      description: End date of the role    
                      format: date    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    name:    
                      description: Name of the role    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    notes:    
                      description: Notes and information about the role    
                      type: string    
                    referrals:    
                      items:    
                        description: A Person data    
                        properties:    
                          avatar:    
                            description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                            properties:    
                              alt:    
                                description: Alternative description of the image    
                                type: string    
                              data:    
                                description: The raw data of the image    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              encoding:    
                                description: The constant value base64 for encoding the images    
                                enum:    
                                  - base64    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              link:    
                                description: 'Link to the stored image '    
                                format: uri    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              mediaType:    
                                description: the media type of the image    
                                enum:    
                                  - image/png    
                                  - image/jpeg    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                            type: object    
                            x-ngsi:    
                              type: Property    
                          birthday:    
                            description: Person's birth date    
                            format: date    
                            type: string    
                          contact:    
                            anyOf:    
                              - properties:    
                                  publicProfiles:    
                                    description: Online services that provide a way to contact a person without exposing mail or phone number.    
                                    items:    
                                      properties:    
                                        URL:    
                                          description: Link to the candidate's profiles    
                                          format: uri    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                        type:    
                                          description: Public profiles in social networks or equivalent resources    
                                          enum:    
                                            - github    
                                            - linkedin    
                                            - manfred    
                                            - other    
                                            - stackoverflow    
                                            - twitter    
                                            - xing    
                                            - website    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                      type: object    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                              - properties:    
                                  phoneNumbers:    
                                    description: Phone numbers to contact the candidate    
                                    items:    
                                      properties:    
                                        countryCode:    
                                          description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                                          type: number    
                                          x-ngsi:    
                                            type: Property    
                                        number:    
                                          description: Phone number without the country prefix    
                                          type: string    
                                          x-ngsi:    
                                            type: Property    
                                      type: object    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                              - properties:    
                                  contactMails:    
                                    description: Contact emails of the candidate    
                                    items:    
                                      description: Every contact email of the candidate    
                                      format: email    
                                      type: string    
                                      x-ngsi:    
                                        type: Property    
                                    type: array    
                                    x-ngsi:    
                                      type: Property    
                                type: object    
                            description: A way to contact a specific person    
                            type: object    
                            x-ngsi:    
                              type: Property    
                          description:    
                            description: Brief bio of the candidate    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          location:    
                            description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                            oneOf:    
                              - description: Geojson reference to the item. Point    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      type: number    
                                    minItems: 2    
                                    type: array    
                                  type:    
                                    enum:    
                                      - Point    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON Point    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. LineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    minItems: 2    
                                    type: array    
                                  type:    
                                    enum:    
                                      - LineString    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON LineString    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. Polygon    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 4    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - Polygon    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON Polygon    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiPoint    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiPoint    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiPoint    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiLineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      minItems: 2    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiLineString    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiLineString    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                              - description: Geojson reference to the item. MultiLineString    
                                properties:    
                                  bbox:    
                                    items:    
                                      type: number    
                                    minItems: 4    
                                    type: array    
                                  coordinates:    
                                    items:    
                                      items:    
                                      type: array    
                                    type: array    
                                  type:    
                                    enum:    
                                      - MultiPolygon    
                                    type: string    
                                required:    
                                  - type    
                                  - coordinates    
                                title: GeoJSON MultiPolygon    
                                type: object    
                                x-ngsi:    
                                  type: GeoProperty    
                            x-ngsi:    
                              type: GeoProperty    
                          name:    
                            description: Name of the candidate    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          surnames:    
                            description: Surname o Surnames of the person    
                            type: string    
                          title:    
                            description: 'Role, relationship or activity related to the person.'    
                            type: string    
                        type: object    
                      type: array    
                    startDate:    
                      description: Start date of the role    
                      format: date    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
              type:    
                description: Types of Projects    
                enum:    
                  - openSource    
                  - other    
                  - personalAchievement    
                  - proBono    
                  - sideProject    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
        publicArtifacts:    
          items:    
            properties:    
              details:    
                description: 'Organization, Company, Institution, Administration, Project or Initiative related to my career.'    
                properties:    
                  URL:    
                    description: 'Link to the site of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    format: uri    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  description:    
                    description: 'Description of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  image:    
                    description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                    properties:    
                      alt:    
                        description: Alternative description of the image    
                        type: string    
                      data:    
                        description: The raw data of the image    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      encoding:    
                        description: The constant value base64 for encoding the images    
                        enum:    
                          - base64    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      link:    
                        description: 'Link to the stored image '    
                        format: uri    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      mediaType:    
                        description: the media type of the image    
                        enum:    
                          - image/png    
                          - image/jpeg    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  location:    
                    description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                    oneOf:    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - Point    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - LineString    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 4    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - Polygon    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPoint    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiLineString    
                          type: string    
                      - bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPolygon    
                          type: string    
                    x-ngsi:    
                      type: GeoProperty    
                  name:    
                    description: 'Name of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              publishingDate:    
                format: date    
                type: string    
              relatedCompetences:    
                items:    
                  description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                  properties:    
                    description:    
                      description: Description of the competence    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    name:    
                      description: Name of the competence    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    type:    
                      description: type of the competence    
                      enum:    
                        - domain    
                        - hardware    
                        - practice    
                        - technology    
                        - tool    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                type: array    
              tags:    
                description: A list of tags with values to provide the candidates a way to segment and categorize elements in their CV.    
                items:    
                  description: 'Every tag description '    
                  type: string    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
              type:    
                description: Types of Public Artifacts    
                enum:    
                  - achievement    
                  - launch    
                  - post    
                  - sideProject    
                  - talk    
                  - video    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    interestingFacts:    
      description: 'Facts that define you: your IDE, your favorite books,  your football team...'    
      items:    
        properties:    
          fact:    
            description: Description of the interesting fact    
            type: string    
            x-ngsi:    
              type: Property    
          topic:    
            description: Topic of the interesting fact    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    knowledge:    
      hardSkills:    
        description: 'Property. HardSkills are a subset of competence types (tool, technology or hardware).'    
        items:    
          properties:    
            level:    
              enum:    
                - basic    
                - expert    
                - high    
                - intermediate    
              type: string    
            skill:    
              description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
              properties:    
                description:    
                  description: Property. Description of the competence    
                  type: string    
                name:    
                  description: Property. Name of the competence    
                  type: string    
                type:    
                  description: Property. type of the competence    
                  enum:    
                    - domain    
                    - hardware    
                    - practice    
                    - technology    
                    - tool    
                  type: string    
              type: object    
          type: object    
        type: array    
      properties:    
        languages:    
          items:    
            properties:    
              fullName:    
                description: A human friendly readable language name    
                type: string    
                x-ngsi:    
                  type: Property    
              level:    
                enum:    
                  - Elementary proficiency    
                  - Limited working proficiency    
                  - Professional working proficiency    
                  - Full professional proficiency    
                  - Native or bilingual proficiency    
                type: string    
              name:    
                description: 'A language expressed as a [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1)'    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
      softSkills:    
        description: Property. SoftSkills are a subset of competence types (practice or domain)    
        items:    
          properties:    
            level:    
              enum:    
                - basic    
                - expert    
                - high    
                - intermediate    
              type: string    
            skill:    
              description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
              properties:    
                description:    
                  description: Property. Description of the competence    
                  type: string    
                name:    
                  description: Property. Name of the competence    
                  type: string    
                type:    
                  description: Property. type of the competence    
                  enum:    
                    - domain    
                    - hardware    
                    - practice    
                    - technology    
                    - tool    
                  type: string    
              type: object    
          type: object    
        type: array    
      studies:    
        items:    
          properties:    
            degreeAchieved:    
              description: Property. If studies finished achieving the linked degree    
              type: boolean    
            description:    
              description: Property. Long description of the study    
              type: string    
            finishDate:    
              description: 'Property. Date when studies finished (if finished), with or without obtaining a degree'    
              format: date    
              type: string    
            institution:    
              description: 'Property. Organization, Company, Institution, Administration, Project or Initiative related to my career.'    
              properties:    
                URL:    
                  description: 'Property. Link to the site of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                  format: uri    
                  type: string    
                description:    
                  description: 'Property. Description of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                  type: string    
                image:    
                  description: 'Property. Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                  properties:    
                    alt:    
                      description: Alternative description of the image    
                      type: string    
                    data:    
                      description: Property. The raw data of the image    
                      type: string    
                    encoding:    
                      description: Property. The constant value base64 for encoding the images    
                      enum:    
                        - base64    
                      type: string    
                    link:    
                      description: 'Property. Link to the stored image '    
                      format: uri    
                      type: string    
                    mediaType:    
                      description: Property. the media type of the image    
                      enum:    
                        - image/png    
                        - image/jpeg    
                      type: string    
                  type: object    
                location:    
                  description: 'GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                  oneOf:    
                    - description: GeoProperty. Geojson reference to the item. Point    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - Point    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON Point    
                      type: object    
                    - description: GeoProperty. Geojson reference to the item. LineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - LineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON LineString    
                      type: object    
                    - description: GeoProperty. Geojson reference to the item. Polygon    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 4    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - Polygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON Polygon    
                      type: object    
                    - description: GeoProperty. Geojson reference to the item. MultiPoint    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPoint    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiPoint    
                      type: object    
                    - description: GeoProperty. Geojson reference to the item. MultiLineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiLineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiLineString    
                      type: object    
                    - description: GeoProperty. Geojson reference to the item. MultiLineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                items:    
                                  type: number    
                                minItems: 2    
                                type: array    
                              minItems: 4    
                              type: array    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPolygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiPolygon    
                      type: object    
                name:    
                  description: 'Property. Name of the Organization, Company, Institution, Administration, Project or Initiative related to my career'    
                  type: string    
              type: object    
            linkedCompetences:    
              items:    
                description: 'Any competence used to complete professional tasks (tools proficiency as ''Excel'', technologies mastered as ''JAVA'', practices learned as ''TDD'', hardware you know how to handle as vehicles or construction tools, and know-how domains as ''banking'' or ''russia'')'    
                properties:    
                  description:    
                    description: Property. Description of the competence    
                    type: string    
                  name:    
                    description: Property. Name of the competence    
                    type: string    
                  type:    
                    description: Property. type of the competence    
                    enum:    
                      - domain    
                      - hardware    
                      - practice    
                      - technology    
                      - tool    
                    type: string    
                type: object    
              type: array    
            name:    
              description: 'Property. Name of the study, in example Software Engineering, Certified ScrumMaster, etc'    
              type: string    
            startDate:    
              description: Property. Date when studies started in ISO 86401format yyyy-mm-dd    
              format: date    
              type: string    
            studyType:    
              description: 'Types of studies: ''officialDegree'' is a degree accredited by the government (University Degree) or an external, recognized and independent agency (some MBAs). ''certification'' is a degree accredited by a private institution (eg. Oracle Database Admin Certification or Project Management Institute PMP). ''unaccredited'' is a course without any accreditation (eg. Coursera or Platzi courses), but this doesn''t mean that is not valid, legit, or has poor quality. ''selfTraining'' is the study designed, managed and evaluated just by the own learner.'    
              enum:    
                - certification    
                - officialDegree    
                - selfTraining    
                - unaccredited    
              type: string    
          type: object    
        type: array    
      type: object    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    noticePeriod:    
      description: Notice period to leave job    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    recommendations:    
      description: Content I like and recommend that can help define me as a professional.    
      items:    
        properties:    
          URL:    
            description: Link to the recommended item    
            type: string    
            x-ngsi:    
              type: Property    
          authors:    
            description: A list of authors of the recommended content    
            items:    
              description: A Person data    
              properties:    
                avatar:    
                  description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
                  properties:    
                    alt:    
                      description: Alternative description of the image    
                      type: string    
                    data:    
                      description: The raw data of the image    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    encoding:    
                      description: The constant value base64 for encoding the images    
                      enum:    
                        - base64    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    link:    
                      description: 'Link to the stored image '    
                      format: uri    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    mediaType:    
                      description: the media type of the image    
                      enum:    
                        - image/png    
                        - image/jpeg    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                birthday:    
                  description: Person's birth date    
                  format: date    
                  type: string    
                contact:    
                  anyOf:    
                    - properties:    
                        publicProfiles:    
                          description: Online services that provide a way to contact a person without exposing mail or phone number.    
                          items:    
                            properties:    
                              URL:    
                                description: Link to the candidate's profiles    
                                format: uri    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              type:    
                                description: Public profiles in social networks or equivalent resources    
                                enum:    
                                  - github    
                                  - linkedin    
                                  - manfred    
                                  - other    
                                  - stackoverflow    
                                  - twitter    
                                  - xing    
                                  - website    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                            type: object    
                          type: array    
                          x-ngsi:    
                            type: Property    
                      type: object    
                    - properties:    
                        phoneNumbers:    
                          description: Phone numbers to contact the candidate    
                          items:    
                            properties:    
                              countryCode:    
                                description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                                type: number    
                                x-ngsi:    
                                  type: Property    
                              number:    
                                description: Phone number without the country prefix    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                            type: object    
                          type: array    
                          x-ngsi:    
                            type: Property    
                      type: object    
                    - properties:    
                        contactMails:    
                          description: Contact emails of the candidate    
                          items:    
                            description: Every contact email of the candidate    
                            format: email    
                            type: string    
                            x-ngsi:    
                              type: Property    
                          type: array    
                          x-ngsi:    
                            type: Property    
                      type: object    
                  description: A way to contact a specific person    
                  type: object    
                  x-ngsi:    
                    type: Property    
                description:    
                  description: Brief bio of the candidate    
                  type: string    
                  x-ngsi:    
                    type: Property    
                location:    
                  description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                  oneOf:    
                    - description: Geojson reference to the item. Point    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - Point    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON Point    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                    - description: Geojson reference to the item. LineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - LineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON LineString    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                    - description: Geojson reference to the item. Polygon    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 4    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - Polygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON Polygon    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                    - description: Geojson reference to the item. MultiPoint    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPoint    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiPoint    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                    - description: Geojson reference to the item. MultiLineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiLineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiLineString    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                    - description: Geojson reference to the item. MultiLineString    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                items:    
                                  type: number    
                                minItems: 2    
                                type: array    
                              minItems: 4    
                              type: array    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPolygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: GeoJSON MultiPolygon    
                      type: object    
                      x-ngsi:    
                        type: GeoProperty    
                  x-ngsi:    
                    type: GeoProperty    
                name:    
                  description: Name of the candidate    
                  type: string    
                  x-ngsi:    
                    type: Property    
                surnames:    
                  description: Surname o Surnames of the person    
                  type: string    
                title:    
                  description: 'Role, relationship or activity related to the person.'    
                  type: string    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          title:    
            description: title of the recommended content    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Types of Recommendations    
            enum:    
              - other    
              - podcast    
              - reading    
              - video    
              - web    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      summary:    
        description: Property. Summary of the recommendations    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    relevantLinks:    
      description: Relevant links of the person    
      items:    
        properties:    
          URL:    
            description: link to the relevant site    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
          description:    
            description: Additional description of the link    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            enum:    
              - github    
              - linkedin    
              - manfred    
              - other    
              - stackoverflow    
              - twitter    
              - xing    
              - website    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    relevantYearsOfExperience:    
      description: Relevant years of experience related with desired professional roles and goals.    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    settings:    
      description: CV Settings    
      properties:    
        language:    
          description: 'The language of the CV expressed as a [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1)'    
          type: string    
          x-ngsi:    
            type: Property    
        lastUpdate:    
          description: Last time the CV was updated    
          format: date    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    significativeRelationships:    
      description: 'Friends or colleagues with whom I have worked or not, whose relationship with me can help define me as a professional.'    
      items:    
        description: A Person data    
        properties:    
          avatar:    
            description: 'Link adn alternative description to the file wth the picture, thumbnail or avatar'    
            properties:    
              alt:    
                description: Alternative description of the image    
                type: string    
              data:    
                description: The raw data of the image    
                type: string    
                x-ngsi:    
                  type: Property    
              encoding:    
                description: The constant value base64 for encoding the images    
                enum:    
                  - base64    
                type: string    
                x-ngsi:    
                  type: Property    
              link:    
                description: 'Link to the stored image '    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
              mediaType:    
                description: the media type of the image    
                enum:    
                  - image/png    
                  - image/jpeg    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          birthday:    
            description: Person's birth date    
            format: date    
            type: string    
          contact:    
            anyOf:    
              - properties:    
                  publicProfiles:    
                    description: Online services that provide a way to contact a person without exposing mail or phone number.    
                    items:    
                      properties:    
                        URL:    
                          description: Link to the candidate's profiles    
                          format: uri    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        type:    
                          description: Public profiles in social networks or equivalent resources    
                          enum:    
                            - github    
                            - linkedin    
                            - manfred    
                            - other    
                            - stackoverflow    
                            - twitter    
                            - xing    
                            - website    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                    type: array    
                    x-ngsi:    
                      type: Property    
                type: object    
              - properties:    
                  phoneNumbers:    
                    description: Phone numbers to contact the candidate    
                    items:    
                      properties:    
                        countryCode:    
                          description: Country calling code as defined in International Telecommunication Union (ITU) standards E.123 and E.164.    
                          type: number    
                          x-ngsi:    
                            type: Property    
                        number:    
                          description: Phone number without the country prefix    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                    type: array    
                    x-ngsi:    
                      type: Property    
                type: object    
              - properties:    
                  contactMails:    
                    description: Contact emails of the candidate    
                    items:    
                      description: Every contact email of the candidate    
                      format: email    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    type: array    
                    x-ngsi:    
                      type: Property    
                type: object    
            description: A way to contact a specific person    
            type: object    
            x-ngsi:    
              type: Property    
          description:    
            description: Brief bio of the candidate    
            type: string    
            x-ngsi:    
              type: Property    
          location:    
            description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf:    
              - description: Geojson reference to the item. Point    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  type:    
                    enum:    
                      - Point    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON Point    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
              - description: Geojson reference to the item. LineString    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      items:    
                        type: number    
                      minItems: 2    
                      type: array    
                    minItems: 2    
                    type: array    
                  type:    
                    enum:    
                      - LineString    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON LineString    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
              - description: Geojson reference to the item. Polygon    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      items:    
                        items:    
                          type: number    
                        minItems: 2    
                        type: array    
                      minItems: 4    
                      type: array    
                    type: array    
                  type:    
                    enum:    
                      - Polygon    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON Polygon    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
              - description: Geojson reference to the item. MultiPoint    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      items:    
                        type: number    
                      minItems: 2    
                      type: array    
                    type: array    
                  type:    
                    enum:    
                      - MultiPoint    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON MultiPoint    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
              - description: Geojson reference to the item. MultiLineString    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      items:    
                        items:    
                          type: number    
                        minItems: 2    
                        type: array    
                      minItems: 2    
                      type: array    
                    type: array    
                  type:    
                    enum:    
                      - MultiLineString    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON MultiLineString    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
              - description: Geojson reference to the item. MultiLineString    
                properties:    
                  bbox:    
                    items:    
                      type: number    
                    minItems: 4    
                    type: array    
                  coordinates:    
                    items:    
                      items:    
                        items:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        minItems: 4    
                        type: array    
                      type: array    
                    type: array    
                  type:    
                    enum:    
                      - MultiPolygon    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                title: GeoJSON MultiPolygon    
                type: object    
                x-ngsi:    
                  type: GeoProperty    
            x-ngsi:    
              type: GeoProperty    
          name:    
            description: Name of the candidate    
            type: string    
            x-ngsi:    
              type: Property    
          surnames:    
            description: Surname o Surnames of the person    
            type: string    
          title:    
            description: 'Role, relationship or activity related to the person.'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Data type. It has to be CurriculumVitae    
      enum:    
        - CurriculumVitae    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://github.com/getmanfred/mac/blob/master/schema/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.HumanResources/blob/master/CurriculumVitae/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.HumanResources/CurriculumVitae/schema.json    
  x-model-tags: Manfred    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### CurriculumVitae NGSI-v2 キー値例  
JSON-LD形式のCurriculumVitaeのkey-valuesの例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HumanResource:001",  
  "type": "CurriculumVitae",  
  "settings": {  
    "language": "ES",  
    "lastUpdate": "2022-02-28"  
  },  
  "aboutMe": {  
    "profile": {  
      "name": "David",  
      "surnames": "Bonilla Fuertes",  
      "title": "Fundador en Manfred / C-Level Executive",  
      "description": "Llevo casi dos décadas desarrollando software, ocupando puestos a lo largo de toda la cadena de valor -programacion, diseño de producto, marketing, ventas y gestión de equipos, departamentos y empresas- pero creo que el rol donde se cruzan mi vocación, mis habilidades y las necesidades de la mayoría de las empresas es en la gestión de equipos y proyectos de construcción de activos digitales.\n\nMe apasiona contribuir en todo el ciclo de vida de un producto o servicio informático, desde la definición hasta el mantenimiento o soporte a clientes, y también involucrarme en la comercialización del mismo.\n\nMe gusta trabajar con gente y para la gente. Como responsable de equipos, mi principal prioridad siempre es eliminar cualquier problema que les impida alcanzar todo su potencial. También procuro devolver a la Comunidad informática parte del valor y el conocimiento que me han aportado a lo largo de mi carrera profesional, dando charlas o colaborando con grupos de usuarios y conferencias técnicas; y, a veces, organizándolos.\n",  
      "avatar": {  
        "alt": "foto de David Bonilla",  
        "link": "https://pbs.twimg.com/profile_images/1387692137664458758/-Z8bTzmY_400x400.jpg"  
      },  
      "birthday": "1977-07-26"  
    },  
    "relevantYearsOfExperience": 20,  
    "relevantLinks": [  
      {  
        "type": "linkedin",  
        "URL": "https://www.linkedin.com/in/dbonillaf/",  
        "description": "Mi perfil en LinkedIn"  
      },  
      {  
        "type": "twitter",  
        "URL": "https://twitter.com/david_bonilla",  
        "description": "Mi cuenta de Twitter"  
      },  
      {  
        "type": "github",  
        "URL": "https://github.com/dbonillaf",  
        "description": "Mi cuenta en GitHub"  
      },  
      {  
        "type": "website",  
        "URL": "https://bonillaware.com/",  
        "description": "Mi Blog"  
      },  
      {  
        "type": "other",  
        "URL": "https://www.bonilista.com",  
        "description": "Mi Newsletter"  
      }  
    ],  
    "significativeRelationships": [  
      {  
        "name": "Diego",  
        "surnames": "Arrola",  
        "title": "Fundador y General Partner del fondo de capital-riesgo K Fund",  
        "description": "Me aporta información sobre el ecosistema startup desde el punto de vista del inversor.",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/inakiarrola"  
            },  
            {  
              "type": "other",  
              "URL": "https://twitter.com/arrola"  
            }  
          ]  
        }  
      },  
      {  
        "name": "Diego",  
        "surnames": "Mariño",  
        "title": "Fundador de Ducksboard y antiguo Principal Product Manager en New Relic",  
        "description": "Amigo con el que siempre valido ideas y estrategias de Product Management.\n",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/diegomarino"  
            }  
          ]  
        }  
      },  
      {  
        "name": "Alberto",  
        "surnames": "Molpeceres",  
        "title": "Fundador de Devengo",  
        "description": "Consulto habitualmente su opinión sobre decisiones importantes a nivel de ejecución y gestión de operaciones.",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/molpe"  
            }  
          ]  
        }  
      }  
    ],  
    "interestingFacts": [  
      {  
        "topic": "First computer",  
        "fact": "Amstrad CPC 464"  
      },  
      {  
        "fact": "Formar parte del equipo que implementó la **pasarela de pago** online del BBVA Definir, diseñar, desarrollar y lanzar un **ERP** y un **WMS** completos, desde cero, en sólo siete años."  
      },  
      {  
        "fact": "Trabajar como **evangelista técnico** en una prometedora startup australiana y dejarla cuando estaba a punto de empezar a cotizar en el NASDAQ, triplicando las ventas en los territorios a mi cargo para contribuir al éxito colectivo."  
      },  
      {  
        "fact": "Lanzar una campaña de **captación de talento técnico** y conseguir atraer a cientos de personas a Madrid para las pruebas de selección y cobertura en TV."  
      },  
      {  
        "fact": "Fundar una **startup** y cerrar una ronda de 330.000€ de inversión de capital-riesgo."  
      },  
      {  
        "fact": "Concebir, desarrollar y lanzar dos productos web que llegaron a transaccionar €1M anuales en **ventas afiliadas**. Vender ambos y gestionar todo el proceso legal previo y posterior."  
      },  
      {  
        "fact": "Enviar una **newsletter** sobre tecnología, todos los domingos desde hace más de seis años, que más de 15.000 personas quieren recibir."  
      },  
      {  
        "fact": "Organizar un evento anual sobre tecnología que vende todas sus entradas en unos pocos segundos."  
      },  
      {  
        "fact": "Ser **CEO** de una compañía fundada por otros."  
      },  
      {  
        "fact": "Gestionar la implementación y cumplimiento de la **LOPD** y el **RGPD**."  
      },  
      {  
        "fact": "Completar todos los trámites legales, operativos y fiscales necesarios para abrir la filial de una compañía multinacional en Bilbao."  
      },  
      {  
        "topic": "¿Cuáles son tus principales herramientas de trabajo (IDEs, editores de texto, clientes de correo, Excel...) y cómo las utilizas (plugins, configuraciones, trucos)?",  
        "fact": "Organizo mi tareas personales con **Passion Planner** (un sistema offline) y las profesionales con **Jira** y **Trello**.Tengo tableros compartidos con distintos equipos de trabajo. Uso labels y fechas de entrega para priorizar mi trabajo.\n\nProgramo HTML/CSS/JavaScript con **Visual Studio Code**. Uso algunas extensiones como ‘GitHistory’, ‘Paste JSON as Code’, o ‘Bookmarks’, pero tanto el trabajo con **Git** como la construcción y la construcción con **Gulp** me gusta hacerlo por línea de comandos.\n\nTambién uso bastante **Postman**, además de para hacer pruebas, directamente como interfaz para APIs REST que tengo en producción."  
      },  
      {  
        "topic": "¿Qué recursos online (webs, blogs, apps, foros, etc) usas para ayudarte a desempeñar tu trabajo?",  
        "fact": "Para informarme de lo más relevante del sector, uso bastante **Twitter** y tengo varias listas específicas por temas. También leo regularmente [Hacker News](https://news.ycombinator.com/) y [Increment](https://increment.com/) y escucho podcasts como[Más que Startups](https://masquestartups.com/).\n\nSi me atasco con algo de código suelo googlear bastante, no tengo un sitio de referencia al que ir, pero muchas veces acabo -supongo que como todos- en [StackOverflow](https://stackoverflow.com/).\n\nPertenezco a un canal de Slack llamado **‘Camaradas del Metal’** donde unas pocas decenas de personas con bastante experiencia suelen comentar y dar contexto a las noticias relacionadas con el emprendimiento tecnológico."  
      },  
      {  
        "topic": "¿Qué nuevas tecnologías y/o herramientas te llaman especialmente la atención y por qué?",  
        "fact": "Soy muy fan de **Git**, no sólo aplicado al código sino prácticamente a cualquier trabajo colaborativo como documentación o contratos.\n\nMe gusta mucho todo el Ecosistema JavaScript que va más allá del navegador (**React**, **Node**) porque me permite trabajar desde el interfaz a la base de datos (con MongoDB) con la misma sintaxis.\n\nTambién me interesa mucho las posibilidades que puede aportar **Blockchain** para cambiar por completo y democratizar el acceso a según qué sectores y nichos, antes vetados a unos pocos."  
      },  
      {  
        "topic": "¿Hay alguna empresa tecnológica que te llame la atención por lo bien que lo está haciendo?",  
        "fact": "Creo que [Microsoft](https://www.microsoft.com/es-es/) está dando los pasos correctos para crear todo un sistema de tooling y despliegue que puede atraer a los programadores.\n\nTambién me gusta todo lo que está construyendo [GitLab](https://about.gitlab.com/) y como lo está vendiendo, con una gran documentación y muchísima transparencia."  
      },  
      {  
        "topic": "¿Cómo intentas mantener actualizados tus conocimientos y habilidades profesionales?",  
        "fact": "Leo todo lo que puedo, pero sobre todo intento hacer pequeños *side projects* que me ayuden a automatizar tareas repetitivas o especialmente pesadas."  
      },  
      {  
        "topic": "¿Sueles compartir tu conocimiento por algún canal (posts, foros, contribución a open source, charlas públicas etc)?",  
        "fact": "Tengo una lista de correo llamada la [Bonilista](https://www.bonilista.com/) en la que escribo un artículo semanal sobre mis experiencias o temas que me interesan. También organizo —junto a más voluntarios— un evento anual sobre construcción de productos/proyectos digitales llamado [Tarugoconf](https://www.tarugoconf.com/) y suelo participar en distintas conferencias y grupos de usuarios."  
      }  
    ],  
    "recommendations": [  
      {  
        "title": "High Output Management",  
        "type": "reading",  
        "authors": [  
          {  
            "name": "Andrew S.",  
            "surnames": "Grove",  
            "title": "Former Chairman and CEO of Intel"  
          }  
        ],  
        "summary": "Un buen manual sobre cómo organizar el trabajo y dirigir equipos para responsables de todos los niveles."  
      }  
    ]  
  },  
  "experience": {  
    "jobs": [  
      {  
        "organization": {  
          "name": "Manfred",  
          "description": "Plataforma de Talento y agencia de recruiting técnico",  
          "URL": "https://www.getmanfred.com/",  
          "image": {  
            "alt": "Logo de Manfred",  
            "link": "https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg"  
          },  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid",  
            "postalCode": "28034",  
            "streetAddress": "Labastida 1"  
          }  
        },  
        "type": "startup",  
        "roles": [  
          {  
            "name": "Fundador",  
            "startDate": "2018-06-20",  
            "challenges": [  
              {  
                "description": "Adaptación de la organización y procesos de la empresa para escalar las operaciones de la misma.",  
                "actions": [  
                  "Implementación de la Holocracia como sistema de gestión.",  
                  "Optimización de los procesos de hiring"  
                ]  
              },  
              {  
                "description": "Desarrollo de producto propio para escalar las operaciones de la compañía, especialmente la aportación de valor a candidatos.",  
                "actions": [  
                  "Definición de visión y alcance de producto.",  
                  "Definición de primer roadmap.",  
                  "Validación de la implementación de funcionalidades."  
                ]  
              },  
              {  
                "description": "Culminación del [proceso de compraventa](https://bonillaware.com/manfred-sngular) de la compañía por parte de Sngular, manteniendo el núcleo de empleados de la compañía y sin que la productividad o las ventas se resintieran antes, durante y después del mismo."  
              },  
              {  
                "description": "Creación y publicación de contratos open source (candidatos y empresas) para construir un marco legal para una empresa de recruiting.",  
                "actions": [  
                  "Definición de alcance y condiciones de contratos para empresas y representados",  
                  "Gestión del repositorio en GitHub para permitir su publicación y consulta así como potenciales pull requests."  
                ]  
              },  
              {  
                "description": "Definición del modelo de datos y los procesos necesarios para identificar, clasificar y gestionar perfiles de profesionales técnicos.",  
                "actions": [  
                  "Proceso de onboarding de representados.",  
                  "Perfilado de candidatos",  
                  "Presentación de representados a potenciales empleadores",  
                  "Recepción de ofertas de empleadores"  
                ]  
              },  
              {  
                "description": "Definición de formato CV extendido.",  
                "actions": [  
                  "Definición de estructura de CV optimizado para búsqueda",  
                  "Creación de plantilla y ejemplos"  
                ]  
              },  
              {  
                "description": "Definición e implementación de la web de la compañía.",  
                "actions": [  
                  "Definición de interfaces",  
                  "Redacción de Copy",  
                  "Implementación de copy y links definitivos en el HTML base"  
                ]  
              },  
              {  
                "description": "Apertura de nueva filial en Bilbao.",  
                "actions": [  
                  "Definición de interfaces",  
                  "Redacción de Copy",  
                  "Implementación de copy y links definitivos en el HTML base"  
                ]  
              }  
            ],  
            "competences": [  
              {  
                "name": "Balsamiq Mockups",  
                "type": "tool",  
                "description": "An app to create low-fi definitions of interfaces"  
              },  
              {  
                "name": "Atlassian Confluence",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian JIRA",  
                "type": "tool"  
              },  
              {  
                "name": "GitHub",  
                "type": "tool"  
              },  
              {  
                "name": "BitBucket",  
                "type": "tool"  
              },  
              {  
                "name": "AWS",  
                "type": "tool"  
              },  
              {  
                "name": "Airtable",  
                "type": "tool"  
              },  
              {  
                "name": "GoogleDocs",  
                "type": "tool"  
              },  
              {  
                "name": "Trello",  
                "type": "tool"  
              },  
              {  
                "name": "Nginx",  
                "type": "tool"  
              },  
              {  
                "name": "Gulp",  
                "type": "tool"  
              },  
              {  
                "name": "VisualStudio Code",  
                "type": "tool"  
              },  
              {  
                "name": "Basecamp",  
                "type": "tool"  
              },  
              {  
                "name": "Less",  
                "type": "technology"  
              },  
              {  
                "name": "NodeJS",  
                "type": "technology"  
              },  
              {  
                "name": "React",  
                "type": "technology"  
              },  
              {  
                "name": "Git",  
                "type": "technology"  
              }  
            ],  
            "referrals": [  
              {  
                "name": "Jose Luis",  
                "surnames": "Vallejo",  
                "title": "Presidente de SNGULAR",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/jlvallejo/"  
                    }  
                  ]  
                }  
              },  
              {  
                "name": "Yago",  
                "surnames": "Cousiño Estevez",  
                "title": "Primer empleado de Manfred",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/yago-cousi%C3%B1o-13533261/"  
                    }  
                  ],  
                  "contactMails": [  
                    "yago@getmanfred.com"  
                  ]  
                }  
              }  
            ]  
          }  
        ]  
      },  
      {  
        "organization": {  
          "name": "Comalatech",  
          "description": "Herramientas para facilitar el trabajo colaborativo en el ecosistema de Atlassian Confluence.",  
          "URL": "https://www.comalatech.com/",  
          "image": {  
            "alt": "Logo de Comalatech",  
            "link": "https://www.comalatech.com/wp-content/themes/comalatech/images/comalatech_logo.png?v=1.0.1"  
          },  
          "address": {  
            "addressCountry": "CA",  
            "addressRegion": "British Columbia",  
            "addressLocality": "Vancouver"  
          }  
        },  
        "type": "startup",  
        "roles": [  
          {  
            "name": "CEO",  
            "startDate": "2017-02-01",  
            "finishDate": "2018-06-30",  
            "challenges": [  
              {  
                "description": "Adaptación de todos los procesos de la compañía al nuevo RGPD",  
                "actions": [  
                  "Definición de requisitos mínimos.",  
                  "Definición de plantillas a cumplimentar por cada nuevo proceso.",  
                  "Documentación de la adecuación de proveedores al reglamento.",  
                  "Definición de la estrategia de petición de consentimiento a usuarios (actuales y nuevos).",  
                  "Redacción de borradores de documentos legales previos a la revisión por departamento legal."  
                ]  
              },  
              {  
                "description": "Apertura de nueva filial en Bilbao",  
                "actions": [  
                  "Documentación y propuesta para aprovechar las ventajas del régimen fiscal y normativo local.",  
                  "Reuniones con Administraciones locales (Diputación y Gobierno Vasco) para alcanzar acuerdos de colaboración previos al establecimiento.",  
                  "Selección y contratación de los primeros empleados.",  
                  "Búsqueda de oficina representativa, adecuación y reforma de la misma.",  
                  "Búsqueda de proveedores locales (fiscalidad y legal)"  
                ]  
              },  
              {  
                "description": "Coordinación de actividades en Europa",  
                "actions": [  
                  "Gestión de personal (contrataciones, finiquitos, incidencias).",  
                  "Establecimiento de centro logístico para materiales de marketing en España.",  
                  "Gestión de la producción de materiales de marketing para distintos eventos."  
                ]  
              },  
              {  
                "description": "Estandarización de contratos",  
                "actions": [  
                  "Diseño de políticas retributivas y condiciones laborales comunes para la plantilla en Canadá y España.",  
                  "Negociación individual con cada uno de los empleados para la aceptación de las nuevas condiciones."  
                ]  
              },  
              {  
                "description": "Soporte"  
              },  
              {  
                "description": "Lanzamiento de Comala Agile Ranking"  
              }  
            ],  
            "competences": [  
              {  
                "name": "Basecamp",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian Confluence",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian JIRA",  
                "type": "tool"  
              },  
              {  
                "name": "BlueJeans Videoconference",  
                "type": "tool"  
              }  
            ],  
            "referrals": [  
              {  
                "name": "Gorka",  
                "surnames": "Puente",  
                "title": "Group Product Manager en Comalatech",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/gorkapuente/"  
                    }  
                  ]  
                }  
              }  
            ]  
          }  
        ]  
      },  
      {  
        "organization": {  
          "name": "Instituto de Empresa"  
        },  
        "type": "academicalInstitution",  
        "roles": [  
          {  
            "name": "Profesor asociado de productividad y metodologías ágiles",  
            "startDate": "2015-04-12"  
          }  
        ]  
      }  
    ],  
    "publicArtifacts": [  
      {  
        "details": {  
          "name": "JSON Schema: dotando a tus datos de un formato y a tus APIs de un contrato | T3chFest 2019",  
          "URL": "https://www.youtube.com/watch?v=KB2DkeQo8d8"  
        },  
        "type": "talk",  
        "publishingDate": "2019-03-22",  
        "relatedCompetences": [  
          {  
            "name": "JSON",  
            "type": "technology"  
          },  
          {  
            "name": "recruiting",  
            "type": "domain"  
          }  
        ],  
        "tags": [  
          "keynotes",  
          "youtube",  
          "t3chfest"  
        ]  
      },  
      {  
        "details": {  
          "name": "Tarugoconf",  
          "description": "Organizador del evento más gallego y awesómico del mundo.",  
          "URL": "https://www.tarugoconf.com/",  
          "image": {  
            "alt": "Logo de la Tarugoconf",  
            "link": "https://www.tarugoconf.com/img/logo-tarugo.png"  
          }  
        },  
        "type": "sideProject"  
      }  
    ]  
  },  
  "knowledge": {  
    "languages": [  
      {  
        "name": "ES",  
        "fullName": "Español",  
        "level": "Native or bilingual proficiency"  
      },  
      {  
        "name": "EN",  
        "level": "Full professional proficiency"  
      },  
      {  
        "name": "GL",  
        "level": "Elementary proficiency"  
      }  
    ],  
    "hardSkills": [  
      {  
        "skill": {  
          "name": "JIRA",  
          "type": "tool",  
          "description": "Administración, configuración y gestión avanzada de JIRA."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "JAVA",  
          "type": "technology"  
        },  
        "level": "high"  
      }  
    ],  
    "softSkills": [  
      {  
        "skill": {  
          "name": "Liderazgo",  
          "type": "practice",  
          "description": "Liderar equipos/organizaciones para que alcancen los objetivos marcados, en tiempo y presupuesto, sin incrementar la rotación de personal."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Atraer talento y retenerlo",  
          "type": "practice"  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Orientado a resultados",  
          "type": "practice",  
          "description": "Acabar proyectos, además de empezarlos."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Comunicación",  
          "type": "practice",  
          "description": "Comunicar lo que hago, cómo lo hago y -sobre todo- por qué lo hago, tanto de forma oral como escrita, con cierta efectividad."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Logística",  
          "type": "domain",  
          "description": "Conocimientos avanzados de aprovisionamiento, almacenamiento, gestión y distribución de bienes"  
        },  
        "level": "high"  
      }  
    ],  
    "studies": [  
      {  
        "studyType": "officialDegree",  
        "degreeAchieved": false,  
        "name": "Ingeniería Técnica Informática",  
        "description": "Computer Science Grade",  
        "startDate": "2002-09-15",  
        "finishDate": "2006-06-30",  
        "institution": {  
          "name": "UOC",  
          "description": "Universitat Oberta de Catalunya",  
          "URL": "https://www.uoc.edu/",  
          "image": {  
            "alt": "logo de UOC",  
            "link": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Logo_UOC.svg"  
          },  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Cataluña",  
            "notes": "Universidad a distancia"  
          }  
        }  
      },  
      {  
        "studyType": "certification",  
        "degreeAchieved": true,  
        "name": "Master en Desarrollo de Aplicaciones Web",  
        "description": "Computer Science Grade",  
        "startDate": "2000-09-15",  
        "finishDate": "2001-06-30",  
        "institution": {  
          "name": "CFDTI IBM/La Caixa",  
          "description": "Centro de Formación de Desarrollo de Tecnologías Informáticas una joint venture de IBM y La Caixa que, desgraciadamente, no perduró en el tiempo.",  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid"  
          }  
        }  
      },  
      {  
        "studyType": "certification",  
        "degreeAchieved": true,  
        "name": "Certified Scrum Master",  
        "description": "Scrum Master certificado por la Scrum Alliance",  
        "startDate": "2007-05-14",  
        "finishDate": "2007-05-21",  
        "institution": {  
          "name": "Scrum Alliance",  
          "description": "Curso de certificación impartido por Ariel Ber",  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid"  
          }  
        }  
      }  
    ]  
  },  
  "careerPreferences": {  
    "contact": {  
      "publicProfiles": [  
        {  
          "type": "manfred",  
          "URL": "https://www.getmanfred.com/mac/david"  
        }  
      ]  
    },  
    "status": "notAvailable",  
    "requirements": {  
      "compensation": {  
        "salary": {  
          "currency": "EUR",  
          "from": 100000  
        },  
        "equity": {  
          "mustHave": true,  
          "from": 10  
        },  
        "perks": {  
          "mustHave": [  
            "Horario Flexible",  
            "BYOD"  
          ],  
          "niceToHave": [  
            "Seguro Médico",  
            "Clases de Idiomas"  
          ]  
        }  
      },  
      "contractTypes": [  
        "permanent",  
        "freelance"  
      ],  
      "situation": {  
        "remoteOnly": false,  
        "openToRelocate": true,  
        "openToRemote": true,  
        "workingAreas": [  
          {  
            "address": {  
              "addressCountry": "ES",  
              "addressRegion": "Galicia",  
              "addressLocality": "A Coruña"  
            },  
            "distanceFromMunicipality": {  
              "unit": "Km",  
              "amount": 20  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "US",  
              "addressRegion": "California"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "US",  
              "addressRegion": "Colorado"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "DE"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "IT"  
            }  
          }  
        ],  
        "comments": "I could consider moving to the States, Germany or Italy if the project is interesting and it makes sense. Otherwise, I prefer to work remotely."  
      }  
    },  
    "preferences": {  
      "preferredCompetences": [  
        {  
          "name": "Agile",  
          "type": "practice",  
          "description": "Gestión ágil"  
        },  
        {  
          "name": "Holocracia",  
          "type": "practice",  
          "description": "Organizaciones Holocráticas"  
        }  
      ],  
      "discardedCompetences": [  
        {  
          "name": "organizaciones jerarquicas",  
          "type": "domain",  
          "description": "No quiero trabajar en un organización muy jerarquizada"  
        },  
        {  
          "name": "juegos de azar",  
          "type": "domain"  
        },  
        {  
          "name": "tabaco",  
          "type": "domain"  
        },  
        {  
          "name": "industria armamentistica",  
          "type": "domain"  
        }  
      ],  
      "preferredOrganizations": [  
        "startup",  
        "academicalInstitution"  
      ],  
      "preferredRoles": [  
        "CEO",  
        "CMO",  
        "CPO"  
      ]  
    },  
    "goals": [  
      {  
        "description": "Me gustaría trabajar en una compañía donde disfrutar de compañeros con orígenes y trayectorias vitales y profesionales diversas, pero que compartan mis valores y mi visión sobre la gestión empresarial en general y el desarrollo de software en particular."  
      },  
      {  
        "title": "Transparencia",  
        "description": "Creo en la transparencia corporativa, en que la actividad, rendimiento, aciertos y fracasos de mis equipos deben ser visibles para el resto de la empresa."  
      },  
      {  
        "description": "Creo que una organización tiene que obsesionarse con cumplir sus objetivos, no con las horas que sus empleados pasan dentro de un edificio."  
      },  
      {  
        "description": "Creo que un buen líder no empuja ni arrastra a un equipo, sino que le señala el objetivo a alcanzar y le ayuda a no alejarse de la ruta para hacerlo."  
      },  
      {  
        "description": "Creo que la construcción de software es un esfuerzo colaborativo y me gusta sentir que mi trabajo ha contribuido al mismo. Pero sobre todo me gusta construir cosas útiles. Tanto como para que la gente esté dispuesta a pagar por ellas."  
      }  
    ]  
  }  
}  
```  
</details>  
#### CurriculumVitae NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の CurriculumVitae の例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HumanResource:001",  
  "type": "CurriculumVitae",  
  "settings": {  
    "type": "StructuredValue",  
    "value": {  
      "language": {  
        "type": "Text",  
        "value": "ES"  
      },  
      "lastUpdate": {  
        "type": "DateTime",  
        "value": "2022-02-28"  
      }  
    }  
  },  
  "aboutMe": {  
    "type": "StructuredValue",  
    "value": {  
      "profile": {  
        "type": "StructuredValue",  
        "value": {  
          "name": {  
            "type": "Text",  
            "value": "David"  
          },  
          "surnames": {  
            "type": "Text",  
            "value": "Bonilla Fuertes"  
          },  
          "title": {  
            "type": "Text",  
            "value": "Fundador en Manfred / C-Level Executive"  
          },  
          "description": {  
            "type": "Text",  
            "value": "Llevo casi dos décadas desarrollando software, ocupando puestos a lo largo de toda la cadena de valor -programacion, diseño de producto, marketing, ventas y gestión de equipos, departamentos y empresas- pero creo que el rol donde se cruzan mi vocación, mis habilidades y las necesidades de la mayoría de las empresas es en la gestión de equipos y proyectos de construcción de activos digitales.\n\nMe apasiona contribuir en todo el ciclo de vida de un producto o servicio informático, desde la definición hasta el mantenimiento o soporte a clientes, y también involucrarme en la comercialización del mismo.\n\nMe gusta trabajar con gente y para la gente. Como responsable de equipos, mi principal prioridad siempre es eliminar cualquier problema que les impida alcanzar todo su potencial. También procuro devolver a la Comunidad informática parte del valor y el conocimiento que me han aportado a lo largo de mi carrera profesional, dando charlas o colaborando con grupos de usuarios y conferencias técnicas; y, a veces, organizándolos.\n"  
          },  
          "avatar": {  
            "type": "StructuredValue",  
            "value": {  
              "alt": {  
                "type": "Text",  
                "value": "foto de David Bonilla"  
              },  
              "link": {  
                "type": "Text",  
                "value": "https://pbs.twimg.com/profile_images/1387692137664458758/-Z8bTzmY_400x400.jpg"  
              }  
            }  
          },  
          "birthday": {  
            "type": "DateTime",  
            "value": "1977-07-26"  
          }  
        }  
      },  
      "relevantYearsOfExperience": {  
        "type": "Number",  
        "value": 20  
      },  
      "relevantLinks": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "type": "linkedin",  
            "URL": {  
              "type": "Text",  
              "value": "https://www.linkedin.com/in/dbonillaf/"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Mi perfil en LinkedIn"  
            }  
          },  
          {  
            "type": "twitter",  
            "URL": {  
              "type": "Text",  
              "value": "https://twitter.com/david_bonilla"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Mi cuenta de Twitter"  
            }  
          },  
          {  
            "type": "github",  
            "URL": {  
              "type": "Text",  
              "value": "https://github.com/dbonillaf"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Mi cuenta en GitHub"  
            }  
          },  
          {  
            "type": "website",  
            "URL": {  
              "type": "Text",  
              "value": "https://bonillaware.com/"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Mi Blog"  
            }  
          },  
          {  
            "type": "other",  
            "URL": {  
              "type": "Text",  
              "value": "https://www.bonilista.com"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Mi Newsletter"  
            }  
          }  
        ]  
      },  
      "significativeRelationships": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "name": {  
              "type": "Text",  
              "value": "Diego"  
            },  
            "surnames": {  
              "type": "Text",  
              "value": "Arrola"  
            },  
            "title": {  
              "type": "Text",  
              "value": "Fundador y General Partner del fondo de capital-riesgo K Fund"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Me aporta información sobre el ecosistema startup desde el punto de vista del inversor."  
            },  
            "contact": {  
              "type": "StructuredValue",  
              "value": {  
                "publicProfiles": {  
                  "type": "StructuredValue",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Text",  
                        "value": "https://www.linkedin.com/in/inakiarrola"  
                      }  
                    },  
                    {  
                      "type": "other",  
                      "URL": {  
                        "type": "Text",  
                        "value": "https://twitter.com/arrola"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          },  
          {  
            "name": {  
              "type": "Text",  
              "value": "Diego"  
            },  
            "surnames": {  
              "type": "Text",  
              "value": "Mariño"  
            },  
            "title": {  
              "type": "Text",  
              "value": "Fundador de Ducksboard y antiguo Principal Product Manager en New Relic"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Amigo con el que siempre valido ideas y estrategias de Product Management.\n"  
            },  
            "contact": {  
              "type": "StructuredValue",  
              "value": {  
                "publicProfiles": {  
                  "type": "StructuredValue",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Text",  
                        "value": "https://www.linkedin.com/in/diegomarino"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          },  
          {  
            "name": {  
              "type": "Text",  
              "value": "Alberto"  
            },  
            "surnames": {  
              "type": "Text",  
              "value": "Molpeceres"  
            },  
            "title": {  
              "type": "Text",  
              "value": "Fundador de Devengo"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Consulto habitualmente su opinión sobre decisiones importantes a nivel de ejecución y gestión de operaciones."  
            },  
            "contact": {  
              "type": "StructuredValue",  
              "value": {  
                "publicProfiles": {  
                  "type": "StructuredValue",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Text",  
                        "value": "https://www.linkedin.com/in/molpe"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          }  
        ]  
      },  
      "interestingFacts": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "topic": {  
              "type": "Text",  
              "value": "First computer"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Amstrad CPC 464"  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Formar parte del equipo que implementó la **pasarela de pago** online del BBVA Definir, diseñar, desarrollar y lanzar un **ERP** y un **WMS** completos, desde cero, en sólo siete años."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Trabajar como **evangelista técnico** en una prometedora startup australiana y dejarla cuando estaba a punto de empezar a cotizar en el NASDAQ, triplicando las ventas en los territorios a mi cargo para contribuir al éxito colectivo."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Lanzar una campaña de **captación de talento técnico** y conseguir atraer a cientos de personas a Madrid para las pruebas de selección y cobertura en TV."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Fundar una **startup** y cerrar una ronda de 330.000€ de inversión de capital-riesgo."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Concebir, desarrollar y lanzar dos productos web que llegaron a transaccionar €1M anuales en **ventas afiliadas**. Vender ambos y gestionar todo el proceso legal previo y posterior."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Enviar una **newsletter** sobre tecnología, todos los domingos desde hace más de seis años, que más de 15.000 personas quieren recibir."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Organizar un evento anual sobre tecnología que vende todas sus entradas en unos pocos segundos."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Ser **CEO** de una compañía fundada por otros."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Gestionar la implementación y cumplimiento de la **LOPD** y el **RGPD**."  
            }  
          },  
          {  
            "fact": {  
              "type": "Text",  
              "value": "Completar todos los trámites legales, operativos y fiscales necesarios para abrir la filial de una compañía multinacional en Bilbao."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Cuáles son tus principales herramientas de trabajo (IDEs, editores de texto, clientes de correo, Excel...) y cómo las utilizas (plugins, configuraciones, trucos)?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Organizo mi tareas personales con **Passion Planner** (un sistema offline) y las profesionales con **Jira** y **Trello**.Tengo tableros compartidos con distintos equipos de trabajo. Uso labels y fechas de entrega para priorizar mi trabajo.\n\nProgramo HTML/CSS/JavaScript con **Visual Studio Code**. Uso algunas extensiones como ‘GitHistory’, ‘Paste JSON as Code’, o ‘Bookmarks’, pero tanto el trabajo con **Git** como la construcción y la construcción con **Gulp** me gusta hacerlo por línea de comandos.\n\nTambién uso bastante **Postman**, además de para hacer pruebas, directamente como interfaz para APIs REST que tengo en producción."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Qué recursos online (webs, blogs, apps, foros, etc) usas para ayudarte a desempeñar tu trabajo?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Para informarme de lo más relevante del sector, uso bastante **Twitter** y tengo varias listas específicas por temas. También leo regularmente [Hacker News](https://news.ycombinator.com/) y [Increment](https://increment.com/) y escucho podcasts como[Más que Startups](https://masquestartups.com/).\n\nSi me atasco con algo de código suelo googlear bastante, no tengo un sitio de referencia al que ir, pero muchas veces acabo -supongo que como todos- en [StackOverflow](https://stackoverflow.com/).\n\nPertenezco a un canal de Slack llamado **‘Camaradas del Metal’** donde unas pocas decenas de personas con bastante experiencia suelen comentar y dar contexto a las noticias relacionadas con el emprendimiento tecnológico."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Qué nuevas tecnologías y/o herramientas te llaman especialmente la atención y por qué?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Soy muy fan de **Git**, no sólo aplicado al código sino prácticamente a cualquier trabajo colaborativo como documentación o contratos.\n\nMe gusta mucho todo el Ecosistema JavaScript que va más allá del navegador (**React**, **Node**) porque me permite trabajar desde el interfaz a la base de datos (con MongoDB) con la misma sintaxis.\n\nTambién me interesa mucho las posibilidades que puede aportar **Blockchain** para cambiar por completo y democratizar el acceso a según qué sectores y nichos, antes vetados a unos pocos."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Hay alguna empresa tecnológica que te llame la atención por lo bien que lo está haciendo?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Creo que [Microsoft](https://www.microsoft.com/es-es/) está dando los pasos correctos para crear todo un sistema de tooling y despliegue que puede atraer a los programadores.\n\nTambién me gusta todo lo que está construyendo [GitLab](https://about.gitlab.com/) y como lo está vendiendo, con una gran documentación y muchísima transparencia."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Cómo intentas mantener actualizados tus conocimientos y habilidades profesionales?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Leo todo lo que puedo, pero sobre todo intento hacer pequeños *side projects* que me ayuden a automatizar tareas repetitivas o especialmente pesadas."  
            }  
          },  
          {  
            "topic": {  
              "type": "Text",  
              "value": "¿Sueles compartir tu conocimiento por algún canal (posts, foros, contribución a open source, charlas públicas etc)?"  
            },  
            "fact": {  
              "type": "Text",  
              "value": "Tengo una lista de correo llamada la [Bonilista](https://www.bonilista.com/) en la que escribo un artículo semanal sobre mis experiencias o temas que me interesan. También organizo —junto a más voluntarios— un evento anual sobre construcción de productos/proyectos digitales llamado [Tarugoconf](https://www.tarugoconf.com/) y suelo participar en distintas conferencias y grupos de usuarios."  
            }  
          }  
        ]  
      },  
      "recommendations": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "title": {  
              "type": "Text",  
              "value": "High Output Management"  
            },  
            "type": "reading",  
            "authors": {  
              "type": "StructuredValue",  
              "value": [  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "Andrew S."  
                  },  
                  "surnames": {  
                    "type": "Text",  
                    "value": "Grove"  
                  },  
                  "title": {  
                    "type": "Text",  
                    "value": "Former Chairman and CEO of Intel"  
                  }  
                }  
              ]  
            },  
            "summary": {  
              "type": "Text",  
              "value": "Un buen manual sobre cómo organizar el trabajo y dirigir equipos para responsables de todos los niveles."  
            }  
          }  
        ]  
      }  
    }  
  },  
  "experience": {  
    "type": "StructuredValue",  
    "value": {  
      "jobs": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "organization": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Manfred"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Plataforma de Talento y agencia de recruiting técnico"  
                },  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.getmanfred.com/"  
                },  
                "image": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "alt": {  
                      "type": "Text",  
                      "value": "Logo de Manfred"  
                    },  
                    "link": {  
                      "type": "Text",  
                      "value": "https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Text",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    },  
                    "postalCode": {  
                      "type": "Text",  
                      "value": "28034"  
                    },  
                    "streetAddress": {  
                      "type": "Text",  
                      "value": "Labastida 1"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "startup",  
            "roles": {  
              "type": "StructuredValue",  
              "value": [  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "Fundador"  
                  },  
                  "startDate": {  
                    "type": "DateTime",  
                    "value": "2018-06-20"  
                  },  
                  "challenges": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Adaptación de la organización y procesos de la empresa para escalar las operaciones de la misma."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Implementación de la Holocracia como sistema de gestión.",  
                            "Optimización de los procesos de hiring"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Desarrollo de producto propio para escalar las operaciones de la compañía, especialmente la aportación de valor a candidatos."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de visión y alcance de producto.",  
                            "Definición de primer roadmap.",  
                            "Validación de la implementación de funcionalidades."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Culminación del [proceso de compraventa](https://bonillaware.com/manfred-sngular) de la compañía por parte de Sngular, manteniendo el núcleo de empleados de la compañía y sin que la productividad o las ventas se resintieran antes, durante y después del mismo."  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Creación y publicación de contratos open source (candidatos y empresas) para construir un marco legal para una empresa de recruiting."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de alcance y condiciones de contratos para empresas y representados",  
                            "Gestión del repositorio en GitHub para permitir su publicación y consulta así como potenciales pull requests."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Definición del modelo de datos y los procesos necesarios para identificar, clasificar y gestionar perfiles de profesionales técnicos."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Proceso de onboarding de representados.",  
                            "Perfilado de candidatos",  
                            "Presentación de representados a potenciales empleadores",  
                            "Recepción de ofertas de empleadores"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Definición de formato CV extendido."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de estructura de CV optimizado para búsqueda",  
                            "Creación de plantilla y ejemplos"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Definición e implementación de la web de la compañía."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de interfaces",  
                            "Redacción de Copy",  
                            "Implementación de copy y links definitivos en el HTML base"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Apertura de nueva filial en Bilbao."  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de interfaces",  
                            "Redacción de Copy",  
                            "Implementación de copy y links definitivos en el HTML base"  
                          ]  
                        }  
                      }  
                    ]  
                  },  
                  "competences": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Balsamiq Mockups"  
                        },  
                        "type": "tool",  
                        "description": {  
                          "type": "Text",  
                          "value": "An app to create low-fi definitions of interfaces"  
                        }  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Atlassian Confluence"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Atlassian JIRA"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "GitHub"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "BitBucket"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "AWS"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Airtable"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "GoogleDocs"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Trello"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Nginx"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Gulp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "VisualStudio Code"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Basecamp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Less"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "NodeJS"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "React"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Git"  
                        },  
                        "type": "technology"  
                      }  
                    ]  
                  },  
                  "referrals": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Jose Luis"  
                        },  
                        "surnames": {  
                          "type": "Text",  
                          "value": "Vallejo"  
                        },  
                        "title": {  
                          "type": "Text",  
                          "value": "Presidente de SNGULAR"  
                        },  
                        "contact": {  
                          "type": "StructuredValue",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "StructuredValue",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Text",  
                                    "value": "https://www.linkedin.com/in/jlvallejo/"  
                                  }  
                                }  
                              ]  
                            }  
                          }  
                        }  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Yago"  
                        },  
                        "surnames": {  
                          "type": "Text",  
                          "value": "Cousiño Estevez"  
                        },  
                        "title": {  
                          "type": "Text",  
                          "value": "Primer empleado de Manfred"  
                        },  
                        "contact": {  
                          "type": "StructuredValue",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "StructuredValue",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Text",  
                                    "value": "https://www.linkedin.com/in/yago-cousi%C3%B1o-13533261/"  
                                  }  
                                }  
                              ]  
                            },  
                            "contactMails": {  
                              "type": "StructuredValue",  
                              "value": [  
                                "yago@getmanfred.com"  
                              ]  
                            }  
                          }  
                        }  
                      }  
                    ]  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "organization": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Comalatech"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Herramientas para facilitar el trabajo colaborativo en el ecosistema de Atlassian Confluence."  
                },  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.comalatech.com/"  
                },  
                "image": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "alt": {  
                      "type": "Text",  
                      "value": "Logo de Comalatech"  
                    },  
                    "link": {  
                      "type": "Text",  
                      "value": "https://www.comalatech.com/wp-content/themes/comalatech/images/comalatech_logo.png?v=1.0.1"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Text",  
                      "value": "CA"  
                    },  
                    "addressRegion": {  
                      "type": "Text",  
                      "value": "British Columbia"  
                    },  
                    "addressLocality": {  
                      "type": "Text",  
                      "value": "Vancouver"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "startup",  
            "roles": {  
              "type": "StructuredValue",  
              "value": [  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "CEO"  
                  },  
                  "startDate": {  
                    "type": "DateTime",  
                    "value": "2017-02-01"  
                  },  
                  "finishDate": {  
                    "type": "DateTime",  
                    "value": "2018-06-30"  
                  },  
                  "challenges": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Adaptación de todos los procesos de la compañía al nuevo RGPD"  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Definición de requisitos mínimos.",  
                            "Definición de plantillas a cumplimentar por cada nuevo proceso.",  
                            "Documentación de la adecuación de proveedores al reglamento.",  
                            "Definición de la estrategia de petición de consentimiento a usuarios (actuales y nuevos).",  
                            "Redacción de borradores de documentos legales previos a la revisión por departamento legal."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Apertura de nueva filial en Bilbao"  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Documentación y propuesta para aprovechar las ventajas del régimen fiscal y normativo local.",  
                            "Reuniones con Administraciones locales (Diputación y Gobierno Vasco) para alcanzar acuerdos de colaboración previos al establecimiento.",  
                            "Selección y contratación de los primeros empleados.",  
                            "Búsqueda de oficina representativa, adecuación y reforma de la misma.",  
                            "Búsqueda de proveedores locales (fiscalidad y legal)"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Coordinación de actividades en Europa"  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Gestión de personal (contrataciones, finiquitos, incidencias).",  
                            "Establecimiento de centro logístico para materiales de marketing en España.",  
                            "Gestión de la producción de materiales de marketing para distintos eventos."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Estandarización de contratos"  
                        },  
                        "actions": {  
                          "type": "StructuredValue",  
                          "value": [  
                            "Diseño de políticas retributivas y condiciones laborales comunes para la plantilla en Canadá y España.",  
                            "Negociación individual con cada uno de los empleados para la aceptación de las nuevas condiciones."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Soporte"  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Text",  
                          "value": "Lanzamiento de Comala Agile Ranking"  
                        }  
                      }  
                    ]  
                  },  
                  "competences": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Basecamp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Atlassian Confluence"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Atlassian JIRA"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "BlueJeans Videoconference"  
                        },  
                        "type": "tool"  
                      }  
                    ]  
                  },  
                  "referrals": {  
                    "type": "StructuredValue",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Text",  
                          "value": "Gorka"  
                        },  
                        "surnames": {  
                          "type": "Text",  
                          "value": "Puente"  
                        },  
                        "title": {  
                          "type": "Text",  
                          "value": "Group Product Manager en Comalatech"  
                        },  
                        "contact": {  
                          "type": "StructuredValue",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "StructuredValue",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Text",  
                                    "value": "https://www.linkedin.com/in/gorkapuente/"  
                                  }  
                                }  
                              ]  
                            }  
                          }  
                        }  
                      }  
                    ]  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "organization": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Instituto de Empresa"  
                }  
              }  
            },  
            "type": "academicalInstitution",  
            "roles": {  
              "type": "StructuredValue",  
              "value": [  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "Profesor asociado de productividad y metodologías ágiles"  
                  },  
                  "startDate": {  
                    "type": "DateTime",  
                    "value": "2015-04-12"  
                  }  
                }  
              ]  
            }  
          }  
        ]  
      },  
      "publicArtifacts": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "details": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "JSON Schema: dotando a tus datos de un formato y a tus APIs de un contrato | T3chFest 2019"  
                },  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.youtube.com/watch?v=KB2DkeQo8d8"  
                }  
              }  
            },  
            "type": "talk",  
            "publishingDate": {  
              "type": "DateTime",  
              "value": "2019-03-22"  
            },  
            "relatedCompetences": {  
              "type": "StructuredValue",  
              "value": [  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "JSON"  
                  },  
                  "type": "technology"  
                },  
                {  
                  "name": {  
                    "type": "Text",  
                    "value": "recruiting"  
                  },  
                  "type": "domain"  
                }  
              ]  
            },  
            "tags": {  
              "type": "StructuredValue",  
              "value": [  
                "keynotes",  
                "youtube",  
                "t3chfest"  
              ]  
            }  
          },  
          {  
            "details": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Tarugoconf"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Organizador del evento más gallego y awesómico del mundo."  
                },  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.tarugoconf.com/"  
                },  
                "image": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "alt": {  
                      "type": "Text",  
                      "value": "Logo de la Tarugoconf"  
                    },  
                    "link": {  
                      "type": "Text",  
                      "value": "https://www.tarugoconf.com/img/logo-tarugo.png"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "sideProject"  
          }  
        ]  
      }  
    }  
  },  
  "knowledge": {  
    "type": "StructuredValue",  
    "value": {  
      "languages": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "name": {  
              "type": "Text",  
              "value": "ES"  
            },  
            "fullName": {  
              "type": "Text",  
              "value": "Español"  
            },  
            "level": {  
              "type": "Text",  
              "value": "Native or bilingual proficiency"  
            }  
          },  
          {  
            "name": {  
              "type": "Text",  
              "value": "EN"  
            },  
            "level": {  
              "type": "Text",  
              "value": "Full professional proficiency"  
            }  
          },  
          {  
            "name": {  
              "type": "Text",  
              "value": "GL"  
            },  
            "level": {  
              "type": "Text",  
              "value": "Elementary proficiency"  
            }  
          }  
        ]  
      },  
      "hardSkills": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "JIRA"  
                },  
                "type": "tool",  
                "description": {  
                  "type": "Text",  
                  "value": "Administración, configuración y gestión avanzada de JIRA."  
                }  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "JAVA"  
                },  
                "type": "technology"  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "high"  
            }  
          }  
        ]  
      },  
      "softSkills": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Liderazgo"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Text",  
                  "value": "Liderar equipos/organizaciones para que alcancen los objetivos marcados, en tiempo y presupuesto, sin incrementar la rotación de personal."  
                }  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Atraer talento y retenerlo"  
                },  
                "type": "practice"  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Orientado a resultados"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Text",  
                  "value": "Acabar proyectos, además de empezarlos."  
                }  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Comunicación"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Text",  
                  "value": "Comunicar lo que hago, cómo lo hago y -sobre todo- por qué lo hago, tanto de forma oral como escrita, con cierta efectividad."  
                }  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Logística"  
                },  
                "type": "domain",  
                "description": {  
                  "type": "Text",  
                  "value": "Conocimientos avanzados de aprovisionamiento, almacenamiento, gestión y distribución de bienes"  
                }  
              }  
            },  
            "level": {  
              "type": "Text",  
              "value": "high"  
            }  
          }  
        ]  
      },  
      "studies": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "studyType": {  
              "type": "Text",  
              "value": "officialDegree"  
            },  
            "degreeAchieved": {  
              "type": "Boolean",  
              "value": false  
            },  
            "name": {  
              "type": "Text",  
              "value": "Ingeniería Técnica Informática"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Computer Science Grade"  
            },  
            "startDate": {  
              "type": "DateTime",  
              "value": "2002-09-15"  
            },  
            "finishDate": {  
              "type": "DateTime",  
              "value": "2006-06-30"  
            },  
            "institution": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "UOC"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Universitat Oberta de Catalunya"  
                },  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.uoc.edu/"  
                },  
                "image": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "alt": {  
                      "type": "Text",  
                      "value": "logo de UOC"  
                    },  
                    "link": {  
                      "type": "Text",  
                      "value": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Logo_UOC.svg"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Text",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Text",  
                      "value": "Cataluña"  
                    },  
                    "notes": {  
                      "type": "Text",  
                      "value": "Universidad a distancia"  
                    }  
                  }  
                }  
              }  
            }  
          },  
          {  
            "studyType": {  
              "type": "Text",  
              "value": "certification"  
            },  
            "degreeAchieved": {  
              "type": "Boolean",  
              "value": true  
            },  
            "name": {  
              "type": "Text",  
              "value": "Master en Desarrollo de Aplicaciones Web"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Computer Science Grade"  
            },  
            "startDate": {  
              "type": "DateTime",  
              "value": "2000-09-15"  
            },  
            "finishDate": {  
              "type": "DateTime",  
              "value": "2001-06-30"  
            },  
            "institution": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "CFDTI IBM/La Caixa"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Centro de Formación de Desarrollo de Tecnologías Informáticas una joint venture de IBM y La Caixa que, desgraciadamente, no perduró en el tiempo."  
                },  
                "address": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Text",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    }  
                  }  
                }  
              }  
            }  
          },  
          {  
            "studyType": {  
              "type": "Text",  
              "value": "certification"  
            },  
            "degreeAchieved": {  
              "type": "Boolean",  
              "value": true  
            },  
            "name": {  
              "type": "Text",  
              "value": "Certified Scrum Master"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Scrum Master certificado por la Scrum Alliance"  
            },  
            "startDate": {  
              "type": "DateTime",  
              "value": "2007-05-14"  
            },  
            "finishDate": {  
              "type": "DateTime",  
              "value": "2007-05-21"  
            },  
            "institution": {  
              "type": "StructuredValue",  
              "value": {  
                "name": {  
                  "type": "Text",  
                  "value": "Scrum Alliance"  
                },  
                "description": {  
                  "type": "Text",  
                  "value": "Curso de certificación impartido por Ariel Ber"  
                },  
                "address": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Text",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Text",  
                      "value": "Madrid"  
                    }  
                  }  
                }  
              }  
            }  
          }  
        ]  
      }  
    }  
  },  
  "careerPreferences": {  
    "type": "StructuredValue",  
    "value": {  
      "contact": {  
        "type": "StructuredValue",  
        "value": {  
          "publicProfiles": {  
            "type": "StructuredValue",  
            "value": [  
              {  
                "type": "manfred",  
                "URL": {  
                  "type": "Text",  
                  "value": "https://www.getmanfred.com/mac/david"  
                }  
              }  
            ]  
          }  
        }  
      },  
      "status": {  
        "type": "Text",  
        "value": "notAvailable"  
      },  
      "requirements": {  
        "type": "StructuredValue",  
        "value": {  
          "compensation": {  
            "type": "StructuredValue",  
            "value": {  
              "salary": {  
                "type": "StructuredValue",  
                "value": {  
                  "currency": {  
                    "type": "Text",  
                    "value": "EUR"  
                  },  
                  "from": {  
                    "type": "Number",  
                    "value": 100000  
                  }  
                }  
              },  
              "equity": {  
                "type": "StructuredValue",  
                "value": {  
                  "mustHave": {  
                    "type": "Boolean",  
                    "value": true  
                  },  
                  "from": {  
                    "type": "Number",  
                    "value": 10  
                  }  
                }  
              },  
              "perks": {  
                "type": "StructuredValue",  
                "value": {  
                  "mustHave": {  
                    "type": "StructuredValue",  
                    "value": [  
                      "Horario Flexible",  
                      "BYOD"  
                    ]  
                  },  
                  "niceToHave": {  
                    "type": "StructuredValue",  
                    "value": [  
                      "Seguro Médico",  
                      "Clases de Idiomas"  
                    ]  
                  }  
                }  
              }  
            }  
          },  
          "contractTypes": {  
            "type": "StructuredValue",  
            "value": [  
              "permanent",  
              "freelance"  
            ]  
          },  
          "situation": {  
            "type": "StructuredValue",  
            "value": {  
              "remoteOnly": {  
                "type": "Boolean",  
                "value": false  
              },  
              "openToRelocate": {  
                "type": "Boolean",  
                "value": true  
              },  
              "openToRemote": {  
                "type": "Boolean",  
                "value": true  
              },  
              "workingAreas": {  
                "type": "StructuredValue",  
                "value": [  
                  {  
                    "address": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Text",  
                          "value": "ES"  
                        },  
                        "addressRegion": {  
                          "type": "Text",  
                          "value": "Galicia"  
                        },  
                        "addressLocality": {  
                          "type": "Text",  
                          "value": "A Coruña"  
                        }  
                      }  
                    },  
                    "distanceFromMunicipality": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "unit": {  
                          "type": "Text",  
                          "value": "Km"  
                        },  
                        "amount": {  
                          "type": "Number",  
                          "value": 20  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Text",  
                          "value": "US"  
                        },  
                        "addressRegion": {  
                          "type": "Text",  
                          "value": "California"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Text",  
                          "value": "US"  
                        },  
                        "addressRegion": {  
                          "type": "Text",  
                          "value": "Colorado"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Text",  
                          "value": "DE"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Text",  
                          "value": "IT"  
                        }  
                      }  
                    }  
                  }  
                ]  
              },  
              "comments": {  
                "type": "Text",  
                "value": "I could consider moving to the States, Germany or Italy if the project is interesting and it makes sense. Otherwise, I prefer to work remotely."  
              }  
            }  
          }  
        }  
      },  
      "preferences": {  
        "type": "StructuredValue",  
        "value": {  
          "preferredCompetences": {  
            "type": "StructuredValue",  
            "value": [  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "Agile"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Text",  
                  "value": "Gestión ágil"  
                }  
              },  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "Holocracia"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Text",  
                  "value": "Organizaciones Holocráticas"  
                }  
              }  
            ]  
          },  
          "discardedCompetences": {  
            "type": "StructuredValue",  
            "value": [  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "organizaciones jerarquicas"  
                },  
                "type": "domain",  
                "description": {  
                  "type": "Text",  
                  "value": "No quiero trabajar en un organización muy jerarquizada"  
                }  
              },  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "juegos de azar"  
                },  
                "type": "domain"  
              },  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "tabaco"  
                },  
                "type": "domain"  
              },  
              {  
                "name": {  
                  "type": "Text",  
                  "value": "industria armamentistica"  
                },  
                "type": "domain"  
              }  
            ]  
          },  
          "preferredOrganizations": {  
            "type": "StructuredValue",  
            "value": [  
              "startup",  
              "academicalInstitution"  
            ]  
          },  
          "preferredRoles": {  
            "type": "StructuredValue",  
            "value": [  
              "CEO",  
              "CMO",  
              "CPO"  
            ]  
          }  
        }  
      },  
      "goals": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "description": {  
              "type": "Text",  
              "value": "Me gustaría trabajar en una compañía donde disfrutar de compañeros con orígenes y trayectorias vitales y profesionales diversas, pero que compartan mis valores y mi visión sobre la gestión empresarial en general y el desarrollo de software en particular."  
            }  
          },  
          {  
            "title": {  
              "type": "Text",  
              "value": "Transparencia"  
            },  
            "description": {  
              "type": "Text",  
              "value": "Creo en la transparencia corporativa, en que la actividad, rendimiento, aciertos y fracasos de mis equipos deben ser visibles para el resto de la empresa."  
            }  
          },  
          {  
            "description": {  
              "type": "Text",  
              "value": "Creo que una organización tiene que obsesionarse con cumplir sus objetivos, no con las horas que sus empleados pasan dentro de un edificio."  
            }  
          },  
          {  
            "description": {  
              "type": "Text",  
              "value": "Creo que un buen líder no empuja ni arrastra a un equipo, sino que le señala el objetivo a alcanzar y le ayuda a no alejarse de la ruta para hacerlo."  
            }  
          },  
          {  
            "description": {  
              "type": "Text",  
              "value": "Creo que la construcción de software es un esfuerzo colaborativo y me gusta sentir que mi trabajo ha contribuido al mismo. Pero sobre todo me gusta construir cosas útiles. Tanto como para que la gente esté dispuesta a pagar por ellas."  
            }  
          }  
        ]  
      }  
    }  
  }  
}  
```  
</details>  
#### CurriculumVitae NGSI-LD キー値の例  
JSON-LD形式のCurriculumVitaeのkey-valuesの例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HumanResource:001",  
  "type": "CurriculumVitae",  
  "settings": {  
    "language": "ES",  
    "lastUpdate": "2022-02-28"  
  },  
  "aboutMe": {  
    "profile": {  
      "name": "David",  
      "surnames": "Bonilla Fuertes",  
      "title": "Fundador en Manfred / C-Level Executive",  
      "description": "Llevo casi dos décadas desarrollando software, ocupando puestos a lo largo de toda la cadena de valor -programacion, diseño de producto, marketing, ventas y gestión de equipos, departamentos y empresas- pero creo que el rol donde se cruzan mi vocación, mis habilidades y las necesidades de la mayoría de las empresas es en la gestión de equipos y proyectos de construcción de activos digitales.\n\nMe apasiona contribuir en todo el ciclo de vida de un producto o servicio informático, desde la definición hasta el mantenimiento o soporte a clientes, y también involucrarme en la comercialización del mismo.\n\nMe gusta trabajar con gente y para la gente. Como responsable de equipos, mi principal prioridad siempre es eliminar cualquier problema que les impida alcanzar todo su potencial. También procuro devolver a la Comunidad informática parte del valor y el conocimiento que me han aportado a lo largo de mi carrera profesional, dando charlas o colaborando con grupos de usuarios y conferencias técnicas; y, a veces, organizándolos.\n",  
      "avatar": {  
        "alt": "foto de David Bonilla",  
        "link": "https://pbs.twimg.com/profile_images/1387692137664458758/-Z8bTzmY_400x400.jpg"  
      },  
      "birthday": "1977-07-26"  
    },  
    "relevantYearsOfExperience": 20,  
    "relevantLinks": [  
      {  
        "type": "linkedin",  
        "URL": "https://www.linkedin.com/in/dbonillaf/",  
        "description": "Mi perfil en LinkedIn"  
      },  
      {  
        "type": "twitter",  
        "URL": "https://twitter.com/david_bonilla",  
        "description": "Mi cuenta de Twitter"  
      },  
      {  
        "type": "github",  
        "URL": "https://github.com/dbonillaf",  
        "description": "Mi cuenta en GitHub"  
      },  
      {  
        "type": "website",  
        "URL": "https://bonillaware.com/",  
        "description": "Mi Blog"  
      },  
      {  
        "type": "other",  
        "URL": "https://www.bonilista.com",  
        "description": "Mi Newsletter"  
      }  
    ],  
    "significativeRelationships": [  
      {  
        "name": "Diego",  
        "surnames": "Arrola",  
        "title": "Fundador y General Partner del fondo de capital-riesgo K Fund",  
        "description": "Me aporta información sobre el ecosistema startup desde el punto de vista del inversor.",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/inakiarrola"  
            },  
            {  
              "type": "other",  
              "URL": "https://twitter.com/arrola"  
            }  
          ]  
        }  
      },  
      {  
        "name": "Diego",  
        "surnames": "Mariño",  
        "title": "Fundador de Ducksboard y antiguo Principal Product Manager en New Relic",  
        "description": "Amigo con el que siempre valido ideas y estrategias de Product Management.\n",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/diegomarino"  
            }  
          ]  
        }  
      },  
      {  
        "name": "Alberto",  
        "surnames": "Molpeceres",  
        "title": "Fundador de Devengo",  
        "description": "Consulto habitualmente su opinión sobre decisiones importantes a nivel de ejecución y gestión de operaciones.",  
        "contact": {  
          "publicProfiles": [  
            {  
              "type": "linkedin",  
              "URL": "https://www.linkedin.com/in/molpe"  
            }  
          ]  
        }  
      }  
    ],  
    "interestingFacts": [  
      {  
        "topic": "First computer",  
        "fact": "Amstrad CPC 464"  
      },  
      {  
        "fact": "Formar parte del equipo que implementó la **pasarela de pago** online del BBVA Definir, diseñar, desarrollar y lanzar un **ERP** y un **WMS** completos, desde cero, en sólo siete años."  
      },  
      {  
        "fact": "Trabajar como **evangelista técnico** en una prometedora startup australiana y dejarla cuando estaba a punto de empezar a cotizar en el NASDAQ, triplicando las ventas en los territorios a mi cargo para contribuir al éxito colectivo."  
      },  
      {  
        "fact": "Lanzar una campaña de **captación de talento técnico** y conseguir atraer a cientos de personas a Madrid para las pruebas de selección y cobertura en TV."  
      },  
      {  
        "fact": "Fundar una **startup** y cerrar una ronda de 330.000€ de inversión de capital-riesgo."  
      },  
      {  
        "fact": "Concebir, desarrollar y lanzar dos productos web que llegaron a transaccionar €1M anuales en **ventas afiliadas**. Vender ambos y gestionar todo el proceso legal previo y posterior."  
      },  
      {  
        "fact": "Enviar una **newsletter** sobre tecnología, todos los domingos desde hace más de seis años, que más de 15.000 personas quieren recibir."  
      },  
      {  
        "fact": "Organizar un evento anual sobre tecnología que vende todas sus entradas en unos pocos segundos."  
      },  
      {  
        "fact": "Ser **CEO** de una compañía fundada por otros."  
      },  
      {  
        "fact": "Gestionar la implementación y cumplimiento de la **LOPD** y el **RGPD**."  
      },  
      {  
        "fact": "Completar todos los trámites legales, operativos y fiscales necesarios para abrir la filial de una compañía multinacional en Bilbao."  
      },  
      {  
        "topic": "¿Cuáles son tus principales herramientas de trabajo (IDEs, editores de texto, clientes de correo, Excel...) y cómo las utilizas (plugins, configuraciones, trucos)?",  
        "fact": "Organizo mi tareas personales con **Passion Planner** (un sistema offline) y las profesionales con **Jira** y **Trello**.Tengo tableros compartidos con distintos equipos de trabajo. Uso labels y fechas de entrega para priorizar mi trabajo.\n\nProgramo HTML/CSS/JavaScript con **Visual Studio Code**. Uso algunas extensiones como ‘GitHistory’, ‘Paste JSON as Code’, o ‘Bookmarks’, pero tanto el trabajo con **Git** como la construcción y la construcción con **Gulp** me gusta hacerlo por línea de comandos.\n\nTambién uso bastante **Postman**, además de para hacer pruebas, directamente como interfaz para APIs REST que tengo en producción."  
      },  
      {  
        "topic": "¿Qué recursos online (webs, blogs, apps, foros, etc) usas para ayudarte a desempeñar tu trabajo?",  
        "fact": "Para informarme de lo más relevante del sector, uso bastante **Twitter** y tengo varias listas específicas por temas. También leo regularmente [Hacker News](https://news.ycombinator.com/) y [Increment](https://increment.com/) y escucho podcasts como[Más que Startups](https://masquestartups.com/).\n\nSi me atasco con algo de código suelo googlear bastante, no tengo un sitio de referencia al que ir, pero muchas veces acabo -supongo que como todos- en [StackOverflow](https://stackoverflow.com/).\n\nPertenezco a un canal de Slack llamado **‘Camaradas del Metal’** donde unas pocas decenas de personas con bastante experiencia suelen comentar y dar contexto a las noticias relacionadas con el emprendimiento tecnológico."  
      },  
      {  
        "topic": "¿Qué nuevas tecnologías y/o herramientas te llaman especialmente la atención y por qué?",  
        "fact": "Soy muy fan de **Git**, no sólo aplicado al código sino prácticamente a cualquier trabajo colaborativo como documentación o contratos.\n\nMe gusta mucho todo el Ecosistema JavaScript que va más allá del navegador (**React**, **Node**) porque me permite trabajar desde el interfaz a la base de datos (con MongoDB) con la misma sintaxis.\n\nTambién me interesa mucho las posibilidades que puede aportar **Blockchain** para cambiar por completo y democratizar el acceso a según qué sectores y nichos, antes vetados a unos pocos."  
      },  
      {  
        "topic": "¿Hay alguna empresa tecnológica que te llame la atención por lo bien que lo está haciendo?",  
        "fact": "Creo que [Microsoft](https://www.microsoft.com/es-es/) está dando los pasos correctos para crear todo un sistema de tooling y despliegue que puede atraer a los programadores.\n\nTambién me gusta todo lo que está construyendo [GitLab](https://about.gitlab.com/) y como lo está vendiendo, con una gran documentación y muchísima transparencia."  
      },  
      {  
        "topic": "¿Cómo intentas mantener actualizados tus conocimientos y habilidades profesionales?",  
        "fact": "Leo todo lo que puedo, pero sobre todo intento hacer pequeños *side projects* que me ayuden a automatizar tareas repetitivas o especialmente pesadas."  
      },  
      {  
        "topic": "¿Sueles compartir tu conocimiento por algún canal (posts, foros, contribución a open source, charlas públicas etc)?",  
        "fact": "Tengo una lista de correo llamada la [Bonilista](https://www.bonilista.com/) en la que escribo un artículo semanal sobre mis experiencias o temas que me interesan. También organizo —junto a más voluntarios— un evento anual sobre construcción de productos/proyectos digitales llamado [Tarugoconf](https://www.tarugoconf.com/) y suelo participar en distintas conferencias y grupos de usuarios."  
      }  
    ],  
    "recommendations": [  
      {  
        "title": "High Output Management",  
        "type": "reading",  
        "authors": [  
          {  
            "name": "Andrew S.",  
            "surnames": "Grove",  
            "title": "Former Chairman and CEO of Intel"  
          }  
        ],  
        "summary": "Un buen manual sobre cómo organizar el trabajo y dirigir equipos para responsables de todos los niveles."  
      }  
    ]  
  },  
  "experience": {  
    "jobs": [  
      {  
        "organization": {  
          "name": "Manfred",  
          "description": "Plataforma de Talento y agencia de recruiting técnico",  
          "URL": "https://www.getmanfred.com/",  
          "image": {  
            "alt": "Logo de Manfred",  
            "link": "https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg"  
          },  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid",  
            "postalCode": "28034",  
            "streetAddress": "Labastida 1"  
          }  
        },  
        "type": "startup",  
        "roles": [  
          {  
            "name": "Fundador",  
            "startDate": "2018-06-20",  
            "challenges": [  
              {  
                "description": "Adaptación de la organización y procesos de la empresa para escalar las operaciones de la misma.",  
                "actions": [  
                  "Implementación de la Holocracia como sistema de gestión.",  
                  "Optimización de los procesos de hiring"  
                ]  
              },  
              {  
                "description": "Desarrollo de producto propio para escalar las operaciones de la compañía, especialmente la aportación de valor a candidatos.",  
                "actions": [  
                  "Definición de visión y alcance de producto.",  
                  "Definición de primer roadmap.",  
                  "Validación de la implementación de funcionalidades."  
                ]  
              },  
              {  
                "description": "Culminación del [proceso de compraventa](https://bonillaware.com/manfred-sngular) de la compañía por parte de Sngular, manteniendo el núcleo de empleados de la compañía y sin que la productividad o las ventas se resintieran antes, durante y después del mismo."  
              },  
              {  
                "description": "Creación y publicación de contratos open source (candidatos y empresas) para construir un marco legal para una empresa de recruiting.",  
                "actions": [  
                  "Definición de alcance y condiciones de contratos para empresas y representados",  
                  "Gestión del repositorio en GitHub para permitir su publicación y consulta así como potenciales pull requests."  
                ]  
              },  
              {  
                "description": "Definición del modelo de datos y los procesos necesarios para identificar, clasificar y gestionar perfiles de profesionales técnicos.",  
                "actions": [  
                  "Proceso de onboarding de representados.",  
                  "Perfilado de candidatos",  
                  "Presentación de representados a potenciales empleadores",  
                  "Recepción de ofertas de empleadores"  
                ]  
              },  
              {  
                "description": "Definición de formato CV extendido.",  
                "actions": [  
                  "Definición de estructura de CV optimizado para búsqueda",  
                  "Creación de plantilla y ejemplos"  
                ]  
              },  
              {  
                "description": "Definición e implementación de la web de la compañía.",  
                "actions": [  
                  "Definición de interfaces",  
                  "Redacción de Copy",  
                  "Implementación de copy y links definitivos en el HTML base"  
                ]  
              },  
              {  
                "description": "Apertura de nueva filial en Bilbao.",  
                "actions": [  
                  "Definición de interfaces",  
                  "Redacción de Copy",  
                  "Implementación de copy y links definitivos en el HTML base"  
                ]  
              }  
            ],  
            "competences": [  
              {  
                "name": "Balsamiq Mockups",  
                "type": "tool",  
                "description": "An app to create low-fi definitions of interfaces"  
              },  
              {  
                "name": "Atlassian Confluence",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian JIRA",  
                "type": "tool"  
              },  
              {  
                "name": "GitHub",  
                "type": "tool"  
              },  
              {  
                "name": "BitBucket",  
                "type": "tool"  
              },  
              {  
                "name": "AWS",  
                "type": "tool"  
              },  
              {  
                "name": "Airtable",  
                "type": "tool"  
              },  
              {  
                "name": "GoogleDocs",  
                "type": "tool"  
              },  
              {  
                "name": "Trello",  
                "type": "tool"  
              },  
              {  
                "name": "Nginx",  
                "type": "tool"  
              },  
              {  
                "name": "Gulp",  
                "type": "tool"  
              },  
              {  
                "name": "VisualStudio Code",  
                "type": "tool"  
              },  
              {  
                "name": "Basecamp",  
                "type": "tool"  
              },  
              {  
                "name": "Less",  
                "type": "technology"  
              },  
              {  
                "name": "NodeJS",  
                "type": "technology"  
              },  
              {  
                "name": "React",  
                "type": "technology"  
              },  
              {  
                "name": "Git",  
                "type": "technology"  
              }  
            ],  
            "referrals": [  
              {  
                "name": "Jose Luis",  
                "surnames": "Vallejo",  
                "title": "Presidente de SNGULAR",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/jlvallejo/"  
                    }  
                  ]  
                }  
              },  
              {  
                "name": "Yago",  
                "surnames": "Cousiño Estevez",  
                "title": "Primer empleado de Manfred",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/yago-cousi%C3%B1o-13533261/"  
                    }  
                  ],  
                  "contactMails": [  
                    "yago@getmanfred.com"  
                  ]  
                }  
              }  
            ]  
          }  
        ]  
      },  
      {  
        "organization": {  
          "name": "Comalatech",  
          "description": "Herramientas para facilitar el trabajo colaborativo en el ecosistema de Atlassian Confluence.",  
          "URL": "https://www.comalatech.com/",  
          "image": {  
            "alt": "Logo de Comalatech",  
            "link": "https://www.comalatech.com/wp-content/themes/comalatech/images/comalatech_logo.png?v=1.0.1"  
          },  
          "address": {  
            "addressCountry": "CA",  
            "addressRegion": "British Columbia",  
            "addressLocality": "Vancouver"  
          }  
        },  
        "type": "startup",  
        "roles": [  
          {  
            "name": "CEO",  
            "startDate": "2017-02-01",  
            "finishDate": "2018-06-30",  
            "challenges": [  
              {  
                "description": "Adaptación de todos los procesos de la compañía al nuevo RGPD",  
                "actions": [  
                  "Definición de requisitos mínimos.",  
                  "Definición de plantillas a cumplimentar por cada nuevo proceso.",  
                  "Documentación de la adecuación de proveedores al reglamento.",  
                  "Definición de la estrategia de petición de consentimiento a usuarios (actuales y nuevos).",  
                  "Redacción de borradores de documentos legales previos a la revisión por departamento legal."  
                ]  
              },  
              {  
                "description": "Apertura de nueva filial en Bilbao",  
                "actions": [  
                  "Documentación y propuesta para aprovechar las ventajas del régimen fiscal y normativo local.",  
                  "Reuniones con Administraciones locales (Diputación y Gobierno Vasco) para alcanzar acuerdos de colaboración previos al establecimiento.",  
                  "Selección y contratación de los primeros empleados.",  
                  "Búsqueda de oficina representativa, adecuación y reforma de la misma.",  
                  "Búsqueda de proveedores locales (fiscalidad y legal)"  
                ]  
              },  
              {  
                "description": "Coordinación de actividades en Europa",  
                "actions": [  
                  "Gestión de personal (contrataciones, finiquitos, incidencias).",  
                  "Establecimiento de centro logístico para materiales de marketing en España.",  
                  "Gestión de la producción de materiales de marketing para distintos eventos."  
                ]  
              },  
              {  
                "description": "Estandarización de contratos",  
                "actions": [  
                  "Diseño de políticas retributivas y condiciones laborales comunes para la plantilla en Canadá y España.",  
                  "Negociación individual con cada uno de los empleados para la aceptación de las nuevas condiciones."  
                ]  
              },  
              {  
                "description": "Soporte"  
              },  
              {  
                "description": "Lanzamiento de Comala Agile Ranking"  
              }  
            ],  
            "competences": [  
              {  
                "name": "Basecamp",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian Confluence",  
                "type": "tool"  
              },  
              {  
                "name": "Atlassian JIRA",  
                "type": "tool"  
              },  
              {  
                "name": "BlueJeans Videoconference",  
                "type": "tool"  
              }  
            ],  
            "referrals": [  
              {  
                "name": "Gorka",  
                "surnames": "Puente",  
                "title": "Group Product Manager en Comalatech",  
                "contact": {  
                  "publicProfiles": [  
                    {  
                      "type": "linkedin",  
                      "URL": "https://www.linkedin.com/in/gorkapuente/"  
                    }  
                  ]  
                }  
              }  
            ]  
          }  
        ]  
      },  
      {  
        "organization": {  
          "name": "Instituto de Empresa"  
        },  
        "type": "academicalInstitution",  
        "roles": [  
          {  
            "name": "Profesor asociado de productividad y metodologías ágiles",  
            "startDate": "2015-04-12"  
          }  
        ]  
      }  
    ],  
    "publicArtifacts": [  
      {  
        "details": {  
          "name": "JSON Schema: dotando a tus datos de un formato y a tus APIs de un contrato | T3chFest 2019",  
          "URL": "https://www.youtube.com/watch?v=KB2DkeQo8d8"  
        },  
        "type": "talk",  
        "publishingDate": "2019-03-22",  
        "relatedCompetences": [  
          {  
            "name": "JSON",  
            "type": "technology"  
          },  
          {  
            "name": "recruiting",  
            "type": "domain"  
          }  
        ],  
        "tags": [  
          "keynotes",  
          "youtube",  
          "t3chfest"  
        ]  
      },  
      {  
        "details": {  
          "name": "Tarugoconf",  
          "description": "Organizador del evento más gallego y awesómico del mundo.",  
          "URL": "https://www.tarugoconf.com/",  
          "image": {  
            "alt": "Logo de la Tarugoconf",  
            "link": "https://www.tarugoconf.com/img/logo-tarugo.png"  
          }  
        },  
        "type": "sideProject"  
      }  
    ]  
  },  
  "knowledge": {  
    "languages": [  
      {  
        "name": "ES",  
        "fullName": "Español",  
        "level": "Native or bilingual proficiency"  
      },  
      {  
        "name": "EN",  
        "level": "Full professional proficiency"  
      },  
      {  
        "name": "GL",  
        "level": "Elementary proficiency"  
      }  
    ],  
    "hardSkills": [  
      {  
        "skill": {  
          "name": "JIRA",  
          "type": "tool",  
          "description": "Administración, configuración y gestión avanzada de JIRA."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "JAVA",  
          "type": "technology"  
        },  
        "level": "high"  
      }  
    ],  
    "softSkills": [  
      {  
        "skill": {  
          "name": "Liderazgo",  
          "type": "practice",  
          "description": "Liderar equipos/organizaciones para que alcancen los objetivos marcados, en tiempo y presupuesto, sin incrementar la rotación de personal."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Atraer talento y retenerlo",  
          "type": "practice"  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Orientado a resultados",  
          "type": "practice",  
          "description": "Acabar proyectos, además de empezarlos."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Comunicación",  
          "type": "practice",  
          "description": "Comunicar lo que hago, cómo lo hago y -sobre todo- por qué lo hago, tanto de forma oral como escrita, con cierta efectividad."  
        },  
        "level": "expert"  
      },  
      {  
        "skill": {  
          "name": "Logística",  
          "type": "domain",  
          "description": "Conocimientos avanzados de aprovisionamiento, almacenamiento, gestión y distribución de bienes"  
        },  
        "level": "high"  
      }  
    ],  
    "studies": [  
      {  
        "studyType": "officialDegree",  
        "degreeAchieved": false,  
        "name": "Ingeniería Técnica Informática",  
        "description": "Computer Science Grade",  
        "startDate": "2002-09-15",  
        "finishDate": "2006-06-30",  
        "institution": {  
          "name": "UOC",  
          "description": "Universitat Oberta de Catalunya",  
          "URL": "https://www.uoc.edu/",  
          "image": {  
            "alt": "logo de UOC",  
            "link": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Logo_UOC.svg"  
          },  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Cataluña",  
            "notes": "Universidad a distancia"  
          }  
        }  
      },  
      {  
        "studyType": "certification",  
        "degreeAchieved": true,  
        "name": "Master en Desarrollo de Aplicaciones Web",  
        "description": "Computer Science Grade",  
        "startDate": "2000-09-15",  
        "finishDate": "2001-06-30",  
        "institution": {  
          "name": "CFDTI IBM/La Caixa",  
          "description": "Centro de Formación de Desarrollo de Tecnologías Informáticas una joint venture de IBM y La Caixa que, desgraciadamente, no perduró en el tiempo.",  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid"  
          }  
        }  
      },  
      {  
        "studyType": "certification",  
        "degreeAchieved": true,  
        "name": "Certified Scrum Master",  
        "description": "Scrum Master certificado por la Scrum Alliance",  
        "startDate": "2007-05-14",  
        "finishDate": "2007-05-21",  
        "institution": {  
          "name": "Scrum Alliance",  
          "description": "Curso de certificación impartido por Ariel Ber",  
          "address": {  
            "addressCountry": "ES",  
            "addressRegion": "Madrid",  
            "addressLocality": "Madrid"  
          }  
        }  
      }  
    ]  
  },  
  "careerPreferences": {  
    "contact": {  
      "publicProfiles": [  
        {  
          "type": "manfred",  
          "URL": "https://www.getmanfred.com/mac/david"  
        }  
      ]  
    },  
    "status": "notAvailable",  
    "requirements": {  
      "compensation": {  
        "salary": {  
          "currency": "EUR",  
          "from": 100000  
        },  
        "equity": {  
          "mustHave": true,  
          "from": 10  
        },  
        "perks": {  
          "mustHave": [  
            "Horario Flexible",  
            "BYOD"  
          ],  
          "niceToHave": [  
            "Seguro Médico",  
            "Clases de Idiomas"  
          ]  
        }  
      },  
      "contractTypes": [  
        "permanent",  
        "freelance"  
      ],  
      "situation": {  
        "remoteOnly": false,  
        "openToRelocate": true,  
        "openToRemote": true,  
        "workingAreas": [  
          {  
            "address": {  
              "addressCountry": "ES",  
              "addressRegion": "Galicia",  
              "addressLocality": "A Coruña"  
            },  
            "distanceFromMunicipality": {  
              "unit": "Km",  
              "amount": 20  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "US",  
              "addressRegion": "California"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "US",  
              "addressRegion": "Colorado"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "DE"  
            }  
          },  
          {  
            "address": {  
              "addressCountry": "IT"  
            }  
          }  
        ],  
        "comments": "I could consider moving to the States, Germany or Italy if the project is interesting and it makes sense. Otherwise, I prefer to work remotely."  
      }  
    },  
    "preferences": {  
      "preferredCompetences": [  
        {  
          "name": "Agile",  
          "type": "practice",  
          "description": "Gestión ágil"  
        },  
        {  
          "name": "Holocracia",  
          "type": "practice",  
          "description": "Organizaciones Holocráticas"  
        }  
      ],  
      "discardedCompetences": [  
        {  
          "name": "organizaciones jerarquicas",  
          "type": "domain",  
          "description": "No quiero trabajar en un organización muy jerarquizada"  
        },  
        {  
          "name": "juegos de azar",  
          "type": "domain"  
        },  
        {  
          "name": "tabaco",  
          "type": "domain"  
        },  
        {  
          "name": "industria armamentistica",  
          "type": "domain"  
        }  
      ],  
      "preferredOrganizations": [  
        "startup",  
        "academicalInstitution"  
      ],  
      "preferredRoles": [  
        "CEO",  
        "CMO",  
        "CPO"  
      ]  
    },  
    "goals": [  
      {  
        "description": "Me gustaría trabajar en una compañía donde disfrutar de compañeros con orígenes y trayectorias vitales y profesionales diversas, pero que compartan mis valores y mi visión sobre la gestión empresarial en general y el desarrollo de software en particular."  
      },  
      {  
        "title": "Transparencia",  
        "description": "Creo en la transparencia corporativa, en que la actividad, rendimiento, aciertos y fracasos de mis equipos deben ser visibles para el resto de la empresa."  
      },  
      {  
        "description": "Creo que una organización tiene que obsesionarse con cumplir sus objetivos, no con las horas que sus empleados pasan dentro de un edificio."  
      },  
      {  
        "description": "Creo que un buen líder no empuja ni arrastra a un equipo, sino que le señala el objetivo a alcanzar y le ayuda a no alejarse de la ruta para hacerlo."  
      },  
      {  
        "description": "Creo que la construcción de software es un esfuerzo colaborativo y me gusta sentir que mi trabajo ha contribuido al mismo. Pero sobre todo me gusta construir cosas útiles. Tanto como para que la gente esté dispuesta a pagar por ellas."  
      }  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.HumanResources/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### CurriculumVitae NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の CurriculumVitae の例である。これは、NGSI-LDと互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HumanResource:001",  
  "type": "CurriculumVitae",  
  "settings": {  
    "type": "Property",  
    "value": {  
      "language": {  
        "type": "Property",  
        "value": "ES"  
      },  
      "lastUpdate": {  
        "type": "Property",  
        "value": {  
          "@type": "date-time",  
          "@value": "2022-02-28"  
        }  
      }  
    }  
  },  
  "aboutMe": {  
    "type": "Property",  
    "value": {  
      "profile": {  
        "type": "Property",  
        "value": {  
          "name": {  
            "type": "Property",  
            "value": "David"  
          },  
          "surnames": {  
            "type": "Property",  
            "value": "Bonilla Fuertes"  
          },  
          "title": {  
            "type": "Property",  
            "value": "Fundador en Manfred / C-Level Executive"  
          },  
          "description": {  
            "type": "Property",  
            "value": "Llevo casi dos décadas desarrollando software, ocupando puestos a lo largo de toda la cadena de valor -programacion, diseño de producto, marketing, ventas y gestión de equipos, departamentos y empresas- pero creo que el rol donde se cruzan mi vocación, mis habilidades y las necesidades de la mayoría de las empresas es en la gestión de equipos y proyectos de construcción de activos digitales.\n\nMe apasiona contribuir en todo el ciclo de vida de un producto o servicio informático, desde la definición hasta el mantenimiento o soporte a clientes, y también involucrarme en la comercialización del mismo.\n\nMe gusta trabajar con gente y para la gente. Como responsable de equipos, mi principal prioridad siempre es eliminar cualquier problema que les impida alcanzar todo su potencial. También procuro devolver a la Comunidad informática parte del valor y el conocimiento que me han aportado a lo largo de mi carrera profesional, dando charlas o colaborando con grupos de usuarios y conferencias técnicas; y, a veces, organizándolos.\n"  
          },  
          "avatar": {  
            "type": "Property",  
            "value": {  
              "alt": {  
                "type": "Property",  
                "value": "foto de David Bonilla"  
              },  
              "link": {  
                "type": "Property",  
                "value": "https://pbs.twimg.com/profile_images/1387692137664458758/-Z8bTzmY_400x400.jpg"  
              }  
            }  
          },  
          "birthday": {  
            "type": "Property",  
            "value": {  
              "@type": "date-time",  
              "@value": "1977-07-26"  
            }  
          }  
        }  
      },  
      "relevantYearsOfExperience": {  
        "type": "Property",  
        "value": 20  
      },  
      "relevantLinks": {  
        "type": "Property",  
        "value": [  
          {  
            "type": "linkedin",  
            "URL": {  
              "type": "Property",  
              "value": "https://www.linkedin.com/in/dbonillaf/"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Mi perfil en LinkedIn"  
            }  
          },  
          {  
            "type": "twitter",  
            "URL": {  
              "type": "Property",  
              "value": "https://twitter.com/david_bonilla"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Mi cuenta de Twitter"  
            }  
          },  
          {  
            "type": "github",  
            "URL": {  
              "type": "Property",  
              "value": "https://github.com/dbonillaf"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Mi cuenta en GitHub"  
            }  
          },  
          {  
            "type": "website",  
            "URL": {  
              "type": "Property",  
              "value": "https://bonillaware.com/"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Mi Blog"  
            }  
          },  
          {  
            "type": "other",  
            "URL": {  
              "type": "Property",  
              "value": "https://www.bonilista.com"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Mi Newsletter"  
            }  
          }  
        ]  
      },  
      "significativeRelationships": {  
        "type": "Property",  
        "value": [  
          {  
            "name": {  
              "type": "Property",  
              "value": "Diego"  
            },  
            "surnames": {  
              "type": "Property",  
              "value": "Arrola"  
            },  
            "title": {  
              "type": "Property",  
              "value": "Fundador y General Partner del fondo de capital-riesgo K Fund"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Me aporta información sobre el ecosistema startup desde el punto de vista del inversor."  
            },  
            "contact": {  
              "type": "Property",  
              "value": {  
                "publicProfiles": {  
                  "type": "Property",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Property",  
                        "value": "https://www.linkedin.com/in/inakiarrola"  
                      }  
                    },  
                    {  
                      "type": "other",  
                      "URL": {  
                        "type": "Property",  
                        "value": "https://twitter.com/arrola"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          },  
          {  
            "name": {  
              "type": "Property",  
              "value": "Diego"  
            },  
            "surnames": {  
              "type": "Property",  
              "value": "Mariño"  
            },  
            "title": {  
              "type": "Property",  
              "value": "Fundador de Ducksboard y antiguo Principal Product Manager en New Relic"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Amigo con el que siempre valido ideas y estrategias de Product Management.\n"  
            },  
            "contact": {  
              "type": "Property",  
              "value": {  
                "publicProfiles": {  
                  "type": "Property",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Property",  
                        "value": "https://www.linkedin.com/in/diegomarino"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          },  
          {  
            "name": {  
              "type": "Property",  
              "value": "Alberto"  
            },  
            "surnames": {  
              "type": "Property",  
              "value": "Molpeceres"  
            },  
            "title": {  
              "type": "Property",  
              "value": "Fundador de Devengo"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Consulto habitualmente su opinión sobre decisiones importantes a nivel de ejecución y gestión de operaciones."  
            },  
            "contact": {  
              "type": "Property",  
              "value": {  
                "publicProfiles": {  
                  "type": "Property",  
                  "value": [  
                    {  
                      "type": "linkedin",  
                      "URL": {  
                        "type": "Property",  
                        "value": "https://www.linkedin.com/in/molpe"  
                      }  
                    }  
                  ]  
                }  
              }  
            }  
          }  
        ]  
      },  
      "interestingFacts": {  
        "type": "Property",  
        "value": [  
          {  
            "topic": {  
              "type": "Property",  
              "value": "First computer"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Amstrad CPC 464"  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Formar parte del equipo que implementó la **pasarela de pago** online del BBVA Definir, diseñar, desarrollar y lanzar un **ERP** y un **WMS** completos, desde cero, en sólo siete años."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Trabajar como **evangelista técnico** en una prometedora startup australiana y dejarla cuando estaba a punto de empezar a cotizar en el NASDAQ, triplicando las ventas en los territorios a mi cargo para contribuir al éxito colectivo."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Lanzar una campaña de **captación de talento técnico** y conseguir atraer a cientos de personas a Madrid para las pruebas de selección y cobertura en TV."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Fundar una **startup** y cerrar una ronda de 330.000€ de inversión de capital-riesgo."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Concebir, desarrollar y lanzar dos productos web que llegaron a transaccionar €1M anuales en **ventas afiliadas**. Vender ambos y gestionar todo el proceso legal previo y posterior."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Enviar una **newsletter** sobre tecnología, todos los domingos desde hace más de seis años, que más de 15.000 personas quieren recibir."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Organizar un evento anual sobre tecnología que vende todas sus entradas en unos pocos segundos."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Ser **CEO** de una compañía fundada por otros."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Gestionar la implementación y cumplimiento de la **LOPD** y el **RGPD**."  
            }  
          },  
          {  
            "fact": {  
              "type": "Property",  
              "value": "Completar todos los trámites legales, operativos y fiscales necesarios para abrir la filial de una compañía multinacional en Bilbao."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Cuáles son tus principales herramientas de trabajo (IDEs, editores de texto, clientes de correo, Excel...) y cómo las utilizas (plugins, configuraciones, trucos)?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Organizo mi tareas personales con **Passion Planner** (un sistema offline) y las profesionales con **Jira** y **Trello**.Tengo tableros compartidos con distintos equipos de trabajo. Uso labels y fechas de entrega para priorizar mi trabajo.\n\nProgramo HTML/CSS/JavaScript con **Visual Studio Code**. Uso algunas extensiones como ‘GitHistory’, ‘Paste JSON as Code’, o ‘Bookmarks’, pero tanto el trabajo con **Git** como la construcción y la construcción con **Gulp** me gusta hacerlo por línea de comandos.\n\nTambién uso bastante **Postman**, además de para hacer pruebas, directamente como interfaz para APIs REST que tengo en producción."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Qué recursos online (webs, blogs, apps, foros, etc) usas para ayudarte a desempeñar tu trabajo?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Para informarme de lo más relevante del sector, uso bastante **Twitter** y tengo varias listas específicas por temas. También leo regularmente [Hacker News](https://news.ycombinator.com/) y [Increment](https://increment.com/) y escucho podcasts como[Más que Startups](https://masquestartups.com/).\n\nSi me atasco con algo de código suelo googlear bastante, no tengo un sitio de referencia al que ir, pero muchas veces acabo -supongo que como todos- en [StackOverflow](https://stackoverflow.com/).\n\nPertenezco a un canal de Slack llamado **‘Camaradas del Metal’** donde unas pocas decenas de personas con bastante experiencia suelen comentar y dar contexto a las noticias relacionadas con el emprendimiento tecnológico."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Qué nuevas tecnologías y/o herramientas te llaman especialmente la atención y por qué?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Soy muy fan de **Git**, no sólo aplicado al código sino prácticamente a cualquier trabajo colaborativo como documentación o contratos.\n\nMe gusta mucho todo el Ecosistema JavaScript que va más allá del navegador (**React**, **Node**) porque me permite trabajar desde el interfaz a la base de datos (con MongoDB) con la misma sintaxis.\n\nTambién me interesa mucho las posibilidades que puede aportar **Blockchain** para cambiar por completo y democratizar el acceso a según qué sectores y nichos, antes vetados a unos pocos."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Hay alguna empresa tecnológica que te llame la atención por lo bien que lo está haciendo?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Creo que [Microsoft](https://www.microsoft.com/es-es/) está dando los pasos correctos para crear todo un sistema de tooling y despliegue que puede atraer a los programadores.\n\nTambién me gusta todo lo que está construyendo [GitLab](https://about.gitlab.com/) y como lo está vendiendo, con una gran documentación y muchísima transparencia."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Cómo intentas mantener actualizados tus conocimientos y habilidades profesionales?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Leo todo lo que puedo, pero sobre todo intento hacer pequeños *side projects* que me ayuden a automatizar tareas repetitivas o especialmente pesadas."  
            }  
          },  
          {  
            "topic": {  
              "type": "Property",  
              "value": "¿Sueles compartir tu conocimiento por algún canal (posts, foros, contribución a open source, charlas públicas etc)?"  
            },  
            "fact": {  
              "type": "Property",  
              "value": "Tengo una lista de correo llamada la [Bonilista](https://www.bonilista.com/) en la que escribo un artículo semanal sobre mis experiencias o temas que me interesan. También organizo —junto a más voluntarios— un evento anual sobre construcción de productos/proyectos digitales llamado [Tarugoconf](https://www.tarugoconf.com/) y suelo participar en distintas conferencias y grupos de usuarios."  
            }  
          }  
        ]  
      },  
      "recommendations": {  
        "type": "Property",  
        "value": [  
          {  
            "title": {  
              "type": "Property",  
              "value": "High Output Management"  
            },  
            "type": "reading",  
            "authors": {  
              "type": "Property",  
              "value": [  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "Andrew S."  
                  },  
                  "surnames": {  
                    "type": "Property",  
                    "value": "Grove"  
                  },  
                  "title": {  
                    "type": "Property",  
                    "value": "Former Chairman and CEO of Intel"  
                  }  
                }  
              ]  
            },  
            "summary": {  
              "type": "Property",  
              "value": "Un buen manual sobre cómo organizar el trabajo y dirigir equipos para responsables de todos los niveles."  
            }  
          }  
        ]  
      }  
    }  
  },  
  "experience": {  
    "type": "Property",  
    "value": {  
      "jobs": {  
        "type": "Property",  
        "value": [  
          {  
            "organization": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Manfred"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Plataforma de Talento y agencia de recruiting técnico"  
                },  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.getmanfred.com/"  
                },  
                "image": {  
                  "type": "Property",  
                  "value": {  
                    "alt": {  
                      "type": "Property",  
                      "value": "Logo de Manfred"  
                    },  
                    "link": {  
                      "type": "Property",  
                      "value": "https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "Property",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Property",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    },  
                    "postalCode": {  
                      "type": "Property",  
                      "value": "28034"  
                    },  
                    "streetAddress": {  
                      "type": "Property",  
                      "value": "Labastida 1"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "startup",  
            "roles": {  
              "type": "Property",  
              "value": [  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "Fundador"  
                  },  
                  "startDate": {  
                    "type": "Property",  
                    "value": {  
                      "@type": "date-time",  
                      "@value": "2018-06-20"  
                    }  
                  },  
                  "challenges": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Adaptación de la organización y procesos de la empresa para escalar las operaciones de la misma."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Implementación de la Holocracia como sistema de gestión.",  
                            "Optimización de los procesos de hiring"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Desarrollo de producto propio para escalar las operaciones de la compañía, especialmente la aportación de valor a candidatos."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de visión y alcance de producto.",  
                            "Definición de primer roadmap.",  
                            "Validación de la implementación de funcionalidades."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Culminación del [proceso de compraventa](https://bonillaware.com/manfred-sngular) de la compañía por parte de Sngular, manteniendo el núcleo de empleados de la compañía y sin que la productividad o las ventas se resintieran antes, durante y después del mismo."  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Creación y publicación de contratos open source (candidatos y empresas) para construir un marco legal para una empresa de recruiting."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de alcance y condiciones de contratos para empresas y representados",  
                            "Gestión del repositorio en GitHub para permitir su publicación y consulta así como potenciales pull requests."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Definición del modelo de datos y los procesos necesarios para identificar, clasificar y gestionar perfiles de profesionales técnicos."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Proceso de onboarding de representados.",  
                            "Perfilado de candidatos",  
                            "Presentación de representados a potenciales empleadores",  
                            "Recepción de ofertas de empleadores"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Definición de formato CV extendido."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de estructura de CV optimizado para búsqueda",  
                            "Creación de plantilla y ejemplos"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Definición e implementación de la web de la compañía."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de interfaces",  
                            "Redacción de Copy",  
                            "Implementación de copy y links definitivos en el HTML base"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Apertura de nueva filial en Bilbao."  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de interfaces",  
                            "Redacción de Copy",  
                            "Implementación de copy y links definitivos en el HTML base"  
                          ]  
                        }  
                      }  
                    ]  
                  },  
                  "competences": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Balsamiq Mockups"  
                        },  
                        "type": "tool",  
                        "description": {  
                          "type": "Property",  
                          "value": "An app to create low-fi definitions of interfaces"  
                        }  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Atlassian Confluence"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Atlassian JIRA"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "GitHub"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "BitBucket"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "AWS"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Airtable"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "GoogleDocs"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Trello"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Nginx"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Gulp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "VisualStudio Code"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Basecamp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Less"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "NodeJS"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "React"  
                        },  
                        "type": "technology"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Git"  
                        },  
                        "type": "technology"  
                      }  
                    ]  
                  },  
                  "referrals": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Jose Luis"  
                        },  
                        "surnames": {  
                          "type": "Property",  
                          "value": "Vallejo"  
                        },  
                        "title": {  
                          "type": "Property",  
                          "value": "Presidente de SNGULAR"  
                        },  
                        "contact": {  
                          "type": "Property",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "Property",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Property",  
                                    "value": "https://www.linkedin.com/in/jlvallejo/"  
                                  }  
                                }  
                              ]  
                            }  
                          }  
                        }  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Yago"  
                        },  
                        "surnames": {  
                          "type": "Property",  
                          "value": "Cousiño Estevez"  
                        },  
                        "title": {  
                          "type": "Property",  
                          "value": "Primer empleado de Manfred"  
                        },  
                        "contact": {  
                          "type": "Property",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "Property",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Property",  
                                    "value": "https://www.linkedin.com/in/yago-cousi%C3%B1o-13533261/"  
                                  }  
                                }  
                              ]  
                            },  
                            "contactMails": {  
                              "type": "Property",  
                              "value": [  
                                "yago@getmanfred.com"  
                              ]  
                            }  
                          }  
                        }  
                      }  
                    ]  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "organization": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Comalatech"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Herramientas para facilitar el trabajo colaborativo en el ecosistema de Atlassian Confluence."  
                },  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.comalatech.com/"  
                },  
                "image": {  
                  "type": "Property",  
                  "value": {  
                    "alt": {  
                      "type": "Property",  
                      "value": "Logo de Comalatech"  
                    },  
                    "link": {  
                      "type": "Property",  
                      "value": "https://www.comalatech.com/wp-content/themes/comalatech/images/comalatech_logo.png?v=1.0.1"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "Property",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Property",  
                      "value": "CA"  
                    },  
                    "addressRegion": {  
                      "type": "Property",  
                      "value": "British Columbia"  
                    },  
                    "addressLocality": {  
                      "type": "Property",  
                      "value": "Vancouver"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "startup",  
            "roles": {  
              "type": "Property",  
              "value": [  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "CEO"  
                  },  
                  "startDate": {  
                    "type": "Property",  
                    "value": {  
                      "@type": "date-time",  
                      "@value": "2017-02-01"  
                    }  
                  },  
                  "finishDate": {  
                    "type": "Property",  
                    "value": {  
                      "@type": "date-time",  
                      "@value": "2018-06-30"  
                    }  
                  },  
                  "challenges": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Adaptación de todos los procesos de la compañía al nuevo RGPD"  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Definición de requisitos mínimos.",  
                            "Definición de plantillas a cumplimentar por cada nuevo proceso.",  
                            "Documentación de la adecuación de proveedores al reglamento.",  
                            "Definición de la estrategia de petición de consentimiento a usuarios (actuales y nuevos).",  
                            "Redacción de borradores de documentos legales previos a la revisión por departamento legal."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Apertura de nueva filial en Bilbao"  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Documentación y propuesta para aprovechar las ventajas del régimen fiscal y normativo local.",  
                            "Reuniones con Administraciones locales (Diputación y Gobierno Vasco) para alcanzar acuerdos de colaboración previos al establecimiento.",  
                            "Selección y contratación de los primeros empleados.",  
                            "Búsqueda de oficina representativa, adecuación y reforma de la misma.",  
                            "Búsqueda de proveedores locales (fiscalidad y legal)"  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Coordinación de actividades en Europa"  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Gestión de personal (contrataciones, finiquitos, incidencias).",  
                            "Establecimiento de centro logístico para materiales de marketing en España.",  
                            "Gestión de la producción de materiales de marketing para distintos eventos."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Estandarización de contratos"  
                        },  
                        "actions": {  
                          "type": "Property",  
                          "value": [  
                            "Diseño de políticas retributivas y condiciones laborales comunes para la plantilla en Canadá y España.",  
                            "Negociación individual con cada uno de los empleados para la aceptación de las nuevas condiciones."  
                          ]  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Soporte"  
                        }  
                      },  
                      {  
                        "description": {  
                          "type": "Property",  
                          "value": "Lanzamiento de Comala Agile Ranking"  
                        }  
                      }  
                    ]  
                  },  
                  "competences": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Basecamp"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Atlassian Confluence"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Atlassian JIRA"  
                        },  
                        "type": "tool"  
                      },  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "BlueJeans Videoconference"  
                        },  
                        "type": "tool"  
                      }  
                    ]  
                  },  
                  "referrals": {  
                    "type": "Property",  
                    "value": [  
                      {  
                        "name": {  
                          "type": "Property",  
                          "value": "Gorka"  
                        },  
                        "surnames": {  
                          "type": "Property",  
                          "value": "Puente"  
                        },  
                        "title": {  
                          "type": "Property",  
                          "value": "Group Product Manager en Comalatech"  
                        },  
                        "contact": {  
                          "type": "Property",  
                          "value": {  
                            "publicProfiles": {  
                              "type": "Property",  
                              "value": [  
                                {  
                                  "type": "linkedin",  
                                  "URL": {  
                                    "type": "Property",  
                                    "value": "https://www.linkedin.com/in/gorkapuente/"  
                                  }  
                                }  
                              ]  
                            }  
                          }  
                        }  
                      }  
                    ]  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "organization": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Instituto de Empresa"  
                }  
              }  
            },  
            "type": "academicalInstitution",  
            "roles": {  
              "type": "Property",  
              "value": [  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "Profesor asociado de productividad y metodologías ágiles"  
                  },  
                  "startDate": {  
                    "type": "Property",  
                    "value": {  
                      "@type": "date-time",  
                      "@value": "2015-04-12"  
                    }  
                  }  
                }  
              ]  
            }  
          }  
        ]  
      },  
      "publicArtifacts": {  
        "type": "Property",  
        "value": [  
          {  
            "details": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "JSON Schema: dotando a tus datos de un formato y a tus APIs de un contrato | T3chFest 2019"  
                },  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.youtube.com/watch?v=KB2DkeQo8d8"  
                }  
              }  
            },  
            "type": "talk",  
            "publishingDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2019-03-22"  
              }  
            },  
            "relatedCompetences": {  
              "type": "Property",  
              "value": [  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "JSON"  
                  },  
                  "type": "technology"  
                },  
                {  
                  "name": {  
                    "type": "Property",  
                    "value": "recruiting"  
                  },  
                  "type": "domain"  
                }  
              ]  
            },  
            "tags": {  
              "type": "Property",  
              "value": [  
                "keynotes",  
                "youtube",  
                "t3chfest"  
              ]  
            }  
          },  
          {  
            "details": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Tarugoconf"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Organizador del evento más gallego y awesómico del mundo."  
                },  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.tarugoconf.com/"  
                },  
                "image": {  
                  "type": "Property",  
                  "value": {  
                    "alt": {  
                      "type": "Property",  
                      "value": "Logo de la Tarugoconf"  
                    },  
                    "link": {  
                      "type": "Property",  
                      "value": "https://www.tarugoconf.com/img/logo-tarugo.png"  
                    }  
                  }  
                }  
              }  
            },  
            "type": "sideProject"  
          }  
        ]  
      }  
    }  
  },  
  "knowledge": {  
    "type": "Property",  
    "value": {  
      "languages": {  
        "type": "Property",  
        "value": [  
          {  
            "name": {  
              "type": "Property",  
              "value": "ES"  
            },  
            "fullName": {  
              "type": "Property",  
              "value": "Español"  
            },  
            "level": {  
              "type": "Property",  
              "value": "Native or bilingual proficiency"  
            }  
          },  
          {  
            "name": {  
              "type": "Property",  
              "value": "EN"  
            },  
            "level": {  
              "type": "Property",  
              "value": "Full professional proficiency"  
            }  
          },  
          {  
            "name": {  
              "type": "Property",  
              "value": "GL"  
            },  
            "level": {  
              "type": "Property",  
              "value": "Elementary proficiency"  
            }  
          }  
        ]  
      },  
      "hardSkills": {  
        "type": "Property",  
        "value": [  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "JIRA"  
                },  
                "type": "tool",  
                "description": {  
                  "type": "Property",  
                  "value": "Administración, configuración y gestión avanzada de JIRA."  
                }  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "JAVA"  
                },  
                "type": "technology"  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "high"  
            }  
          }  
        ]  
      },  
      "softSkills": {  
        "type": "Property",  
        "value": [  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Liderazgo"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Property",  
                  "value": "Liderar equipos/organizaciones para que alcancen los objetivos marcados, en tiempo y presupuesto, sin incrementar la rotación de personal."  
                }  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Atraer talento y retenerlo"  
                },  
                "type": "practice"  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Orientado a resultados"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Property",  
                  "value": "Acabar proyectos, además de empezarlos."  
                }  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Comunicación"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Property",  
                  "value": "Comunicar lo que hago, cómo lo hago y -sobre todo- por qué lo hago, tanto de forma oral como escrita, con cierta efectividad."  
                }  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "expert"  
            }  
          },  
          {  
            "skill": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Logística"  
                },  
                "type": "domain",  
                "description": {  
                  "type": "Property",  
                  "value": "Conocimientos avanzados de aprovisionamiento, almacenamiento, gestión y distribución de bienes"  
                }  
              }  
            },  
            "level": {  
              "type": "Property",  
              "value": "high"  
            }  
          }  
        ]  
      },  
      "studies": {  
        "type": "Property",  
        "value": [  
          {  
            "studyType": {  
              "type": "Property",  
              "value": "officialDegree"  
            },  
            "degreeAchieved": {  
              "type": "Property",  
              "value": false  
            },  
            "name": {  
              "type": "Property",  
              "value": "Ingeniería Técnica Informática"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Computer Science Grade"  
            },  
            "startDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2002-09-15"  
              }  
            },  
            "finishDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2006-06-30"  
              }  
            },  
            "institution": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "UOC"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Universitat Oberta de Catalunya"  
                },  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.uoc.edu/"  
                },  
                "image": {  
                  "type": "Property",  
                  "value": {  
                    "alt": {  
                      "type": "Property",  
                      "value": "logo de UOC"  
                    },  
                    "link": {  
                      "type": "Property",  
                      "value": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Logo_UOC.svg"  
                    }  
                  }  
                },  
                "address": {  
                  "type": "Property",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Property",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Property",  
                      "value": "Cataluña"  
                    },  
                    "notes": {  
                      "type": "Property",  
                      "value": "Universidad a distancia"  
                    }  
                  }  
                }  
              }  
            }  
          },  
          {  
            "studyType": {  
              "type": "Property",  
              "value": "certification"  
            },  
            "degreeAchieved": {  
              "type": "Property",  
              "value": true  
            },  
            "name": {  
              "type": "Property",  
              "value": "Master en Desarrollo de Aplicaciones Web"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Computer Science Grade"  
            },  
            "startDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2000-09-15"  
              }  
            },  
            "finishDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2001-06-30"  
              }  
            },  
            "institution": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "CFDTI IBM/La Caixa"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Centro de Formación de Desarrollo de Tecnologías Informáticas una joint venture de IBM y La Caixa que, desgraciadamente, no perduró en el tiempo."  
                },  
                "address": {  
                  "type": "Property",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Property",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    }  
                  }  
                }  
              }  
            }  
          },  
          {  
            "studyType": {  
              "type": "Property",  
              "value": "certification"  
            },  
            "degreeAchieved": {  
              "type": "Property",  
              "value": true  
            },  
            "name": {  
              "type": "Property",  
              "value": "Certified Scrum Master"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Scrum Master certificado por la Scrum Alliance"  
            },  
            "startDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2007-05-14"  
              }  
            },  
            "finishDate": {  
              "type": "Property",  
              "value": {  
                "@type": "date-time",  
                "@value": "2007-05-21"  
              }  
            },  
            "institution": {  
              "type": "Property",  
              "value": {  
                "name": {  
                  "type": "Property",  
                  "value": "Scrum Alliance"  
                },  
                "description": {  
                  "type": "Property",  
                  "value": "Curso de certificación impartido por Ariel Ber"  
                },  
                "address": {  
                  "type": "Property",  
                  "value": {  
                    "addressCountry": {  
                      "type": "Property",  
                      "value": "ES"  
                    },  
                    "addressRegion": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    },  
                    "addressLocality": {  
                      "type": "Property",  
                      "value": "Madrid"  
                    }  
                  }  
                }  
              }  
            }  
          }  
        ]  
      }  
    }  
  },  
  "careerPreferences": {  
    "type": "Property",  
    "value": {  
      "contact": {  
        "type": "Property",  
        "value": {  
          "publicProfiles": {  
            "type": "Property",  
            "value": [  
              {  
                "type": "manfred",  
                "URL": {  
                  "type": "Property",  
                  "value": "https://www.getmanfred.com/mac/david"  
                }  
              }  
            ]  
          }  
        }  
      },  
      "status": {  
        "type": "Property",  
        "value": "notAvailable"  
      },  
      "requirements": {  
        "type": "Property",  
        "value": {  
          "compensation": {  
            "type": "Property",  
            "value": {  
              "salary": {  
                "type": "Property",  
                "value": {  
                  "currency": {  
                    "type": "Property",  
                    "value": "EUR"  
                  },  
                  "from": {  
                    "type": "Property",  
                    "value": 100000  
                  }  
                }  
              },  
              "equity": {  
                "type": "Property",  
                "value": {  
                  "mustHave": {  
                    "type": "Property",  
                    "value": true  
                  },  
                  "from": {  
                    "type": "Property",  
                    "value": 10  
                  }  
                }  
              },  
              "perks": {  
                "type": "Property",  
                "value": {  
                  "mustHave": {  
                    "type": "Property",  
                    "value": [  
                      "Horario Flexible",  
                      "BYOD"  
                    ]  
                  },  
                  "niceToHave": {  
                    "type": "Property",  
                    "value": [  
                      "Seguro Médico",  
                      "Clases de Idiomas"  
                    ]  
                  }  
                }  
              }  
            }  
          },  
          "contractTypes": {  
            "type": "Property",  
            "value": [  
              "permanent",  
              "freelance"  
            ]  
          },  
          "situation": {  
            "type": "Property",  
            "value": {  
              "remoteOnly": {  
                "type": "Property",  
                "value": false  
              },  
              "openToRelocate": {  
                "type": "Property",  
                "value": true  
              },  
              "openToRemote": {  
                "type": "Property",  
                "value": true  
              },  
              "workingAreas": {  
                "type": "Property",  
                "value": [  
                  {  
                    "address": {  
                      "type": "Property",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Property",  
                          "value": "ES"  
                        },  
                        "addressRegion": {  
                          "type": "Property",  
                          "value": "Galicia"  
                        },  
                        "addressLocality": {  
                          "type": "Property",  
                          "value": "A Coruña"  
                        }  
                      }  
                    },  
                    "distanceFromMunicipality": {  
                      "type": "Property",  
                      "value": {  
                        "unit": {  
                          "type": "Property",  
                          "value": "Km"  
                        },  
                        "amount": {  
                          "type": "Property",  
                          "value": 20  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "Property",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Property",  
                          "value": "US"  
                        },  
                        "addressRegion": {  
                          "type": "Property",  
                          "value": "California"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "Property",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Property",  
                          "value": "US"  
                        },  
                        "addressRegion": {  
                          "type": "Property",  
                          "value": "Colorado"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "Property",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Property",  
                          "value": "DE"  
                        }  
                      }  
                    }  
                  },  
                  {  
                    "address": {  
                      "type": "Property",  
                      "value": {  
                        "addressCountry": {  
                          "type": "Property",  
                          "value": "IT"  
                        }  
                      }  
                    }  
                  }  
                ]  
              },  
              "comments": {  
                "type": "Property",  
                "value": "I could consider moving to the States, Germany or Italy if the project is interesting and it makes sense. Otherwise, I prefer to work remotely."  
              }  
            }  
          }  
        }  
      },  
      "preferences": {  
        "type": "Property",  
        "value": {  
          "preferredCompetences": {  
            "type": "Property",  
            "value": [  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "Agile"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Property",  
                  "value": "Gestión ágil"  
                }  
              },  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "Holocracia"  
                },  
                "type": "practice",  
                "description": {  
                  "type": "Property",  
                  "value": "Organizaciones Holocráticas"  
                }  
              }  
            ]  
          },  
          "discardedCompetences": {  
            "type": "Property",  
            "value": [  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "organizaciones jerarquicas"  
                },  
                "type": "domain",  
                "description": {  
                  "type": "Property",  
                  "value": "No quiero trabajar en un organización muy jerarquizada"  
                }  
              },  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "juegos de azar"  
                },  
                "type": "domain"  
              },  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "tabaco"  
                },  
                "type": "domain"  
              },  
              {  
                "name": {  
                  "type": "Property",  
                  "value": "industria armamentistica"  
                },  
                "type": "domain"  
              }  
            ]  
          },  
          "preferredOrganizations": {  
            "type": "Property",  
            "value": [  
              "startup",  
              "academicalInstitution"  
            ]  
          },  
          "preferredRoles": {  
            "type": "Property",  
            "value": [  
              "CEO",  
              "CMO",  
              "CPO"  
            ]  
          }  
        }  
      },  
      "goals": {  
        "type": "Property",  
        "value": [  
          {  
            "description": {  
              "type": "Property",  
              "value": "Me gustaría trabajar en una compañía donde disfrutar de compañeros con orígenes y trayectorias vitales y profesionales diversas, pero que compartan mis valores y mi visión sobre la gestión empresarial en general y el desarrollo de software en particular."  
            }  
          },  
          {  
            "title": {  
              "type": "Property",  
              "value": "Transparencia"  
            },  
            "description": {  
              "type": "Property",  
              "value": "Creo en la transparencia corporativa, en que la actividad, rendimiento, aciertos y fracasos de mis equipos deben ser visibles para el resto de la empresa."  
            }  
          },  
          {  
            "description": {  
              "type": "Property",  
              "value": "Creo que una organización tiene que obsesionarse con cumplir sus objetivos, no con las horas que sus empleados pasan dentro de un edificio."  
            }  
          },  
          {  
            "description": {  
              "type": "Property",  
              "value": "Creo que un buen líder no empuja ni arrastra a un equipo, sino que le señala el objetivo a alcanzar y le ayuda a no alejarse de la ruta para hacerlo."  
            }  
          },  
          {  
            "description": {  
              "type": "Property",  
              "value": "Creo que la construcción de software es un esfuerzo colaborativo y me gusta sentir que mi trabajo ha contribuido al mismo. Pero sobre todo me gusta construir cosas útiles. Tanto como para que la gente esté dispuesta a pagar por ellas."  
            }  
          }  
        ]  
      }  
    }  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
