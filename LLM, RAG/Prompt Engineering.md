# Prompot Engineering

## 프롬프트 엔지니어링(Prompt Engineering)

- AI 모델, 특히 LLM에 적절한 입력을 설계하고 작성, 모델이 최적의 응답을 하도록 유도하는 기술.

- GPT 모델 같은 LLM은 입력된 프롬프트에 따라 답변을 생성, 잘 설계된 프롬프트는 정확하고 유용한 결과를 얻을 수 있고, 잘못된 프롬프트는 부정확하고 혼란스러운 결과를 얻을 수 있음.

__목표__  

    - 모델이 의도한 대로 응답하도록 유도하는 것.
    - 프롬프트의 구조나 어조를 조정해, 답변의 품질과 일관성을 높이는 것이 중요.

### 프롬프트 엔지니어링이 동작하는 이유

- LLM은 기본적으로 '__패턴 인식__'과 '__확률 계산__'에 기반하여 학습됨.
- 학습 데이터 내에서 어떤 단어가 어떤 맥락에서 자주 등장하는지를 학습하고, 주어진 프롬프트에 맞는 답을 확률적으로 생성.
- 모델의 패턴 학습 메커니즘을 활용하여 모델이 적절한 경로로 답을 유도하도록 하는 방법.

#### 동작 원리

1. __프롬프트 입력__ : 사용자가 모델에 질문이나 요청 입력.

2. __맥락 파악__ : 입력된 프롬프트 기반으로 맥락 분석, 그에 맞는 적절한 답변 생성.

3. __확률 계산__ : 학습된 데이터를 기반으로 각 단어나 문장의 확률 분포를 계산해, 가장 가능성 높은 답변을 선택.

- 프롬프트 엔지니어링은 위 과정들을 최적화하기 위한 방법. 더 나은 답변을 얻기 위해 명확, 구체적 입력을 작성하는 것.

### System, Assistant, User 역할 적용

1. __User(사용자)__

    - 모델과 대화하는 주체, 질문이나 요구사항을 제시하는 역할.
    - Prompt Engineering에서 User Prompt는 명확한 요청을 포함해야 하고, 의도가 분명해야 함. User는 모델이 무엇을 해야 하는지 정확하게 전달해야 하므로, 질문 형태의 프롬프트가 많음.

2. __Assistant(도우미)__

    - User의 질문에 답변을 제공하는 역할, 실제 GPT 모델이 수행하는 부분.
    - User가 입력한 내용에 따라 질문의 맥락에 적절하고 일관성 있는 답변을 생성해야 하며, 명확한 어조와 친절한 태도로 응답하는 것이 일반적.

3. __System(시스템)__

    - 대화의 기본 규칙과 Assistant의 성격을 결정. 대화의 배경, 규칙을 설정하여 모델이 답변을 생성할 때 어떤 스타일과 어조를 사용할지 지시 가능.
    - System Prompt는 모델이 특정한 태도나 전문성을 갖고 응답하도록 프레임워크를 제공.
    - 또한 Assistant의 행동을 가이드하는 역할을 함. 대화의 일관성을 유지하고, 특정한 목적에 맞게 답변을 최적화할 수 있음.

### 프롬프트 엔지니어링 적용 예시

1. 일반적인 대화 흐름 설정

    - System: "Assistant는 친절하고 명확한 설명을 제공합니다."
    - User: "산업 혁명이 시작된 배경에 대해 알려주세요."
    - Assistant: "산업 혁명은 18세기 후반 영국에서 시작되었으며, 기술 혁신과 경제적 변화가 그 주요 배경입니다. 특히 기계화와 공장 시스템의 발전이 큰 역할을 했습니다."

2. 전문적이고 깊이 있는 답변을 원할 때

    - System: "Assistant는 역사 전문가로서 깊이 있는 설명을 제공하며, 중요한 역사적 배경도 함께 다룹니다."
    - User: "영국의 산업 혁명의 주요 원인에 대해 설명해 주세요."
    - Assistant: "산업 혁명의 주요 원인 중 하나는 영국의 풍부한 천연 자원, 특히 석탄과 철광석의 이용 가능성입니다. 또한, 상업의 발전과 대규모 자본 축적, 정치적 안정성 등이 중요한 역할을 했습니다. 이 외에도 농업 혁명으로 인한 노동력의 증가도 큰 원인이었습니다..."

3. 간결한 답변만 원할 때

    - System: "Assistant는 간결하고 핵심만을 전달하는 답변을 제공합니다."
    - User: "산업 혁명의 주요 발명품은 무엇인가요?"
    - Assistant: "산업 혁명의 주요 발명품으로는 방적기, 증기기관, 코튼 진 등이 있습니다."

### 주의할 점

1. __명확하고 구체적인 프롬프트 작성__ : 모델이 혼란을 겪지 않도록 모호한 질문 추상적 요청은 피하고, 어떤 결과를 기대하는지 명확히 표현하는 것이 중요.

2. __맥락 유지__ : LLM은 이전의 대화내용을 기반으로 답변 생성, 맥락 유지가 중요. 이전 대화와의 연결성을 고려해야 함.

3. __System 설정의 중요성__ : 응답 스타일, 태도에 큰 영향 미침. 올바른 설정은 대화의 질을 높이고, 사용자가 원하는 특정 답변 스타일을 확보 가능.

## 프롬프트 엔지니어링(Prompt Engineering) 기본 원칙

- __명확한 요청__, __정보 제공__, __제약 조건 설정__, __작업 분할__
- 기본 원칙을 이해하기 위해 직접 OpenAI Playground에서 실습 진행하였음. 아래 예시는 직접 실행한 결과임.

### 명확한 요청

- 너무 추상적이거나 모호한 요청을 하면, 모델이 혼란스럽거나 부정확한 답을 줄 수 있어 명확한 요청이 필수.

    Ex. 추상적인 요청  
        - User : 잘생긴 연예인에 대해 알려줘
        - Assistant : 잘생긴 연예인은 주관적인 의견에 따라 다르지만, 많은 사람들이 동의하는 몇몇 한국 연예인을 소개할 수 있습니다.

    Ex. 구체적인 요청
        - User : 한국영화 '아저씨'에서 주연이었던 남자 배우에 대해 알려줘
        - Assistant : 한국 영화 '아저씨'의 주연 배우는 원빈입니다. 원빈은 영화에서 차태식 역을 맡아 인상적인 연기를 펼쳤습니다. '아저씨'는 2010년에 개봉했으며, 그는 영화에서 과묵하지만 뛰어난 전투 능력을 가진 인물로 출연했습니다. 원빈은 이 역할을 통해 강한 카리스마와 액션 연기로 많은 찬사를 받았으며, 이 영화는 그의 필모그래피에서 중요한 작품 중 하나로 꼽힙니다. '아저씨'는 흥행에 성공했을 뿐만 아니라, 원빈의 연기 경력에 있어서도 한 획을 그은 작품입니다.

### 정보 제공

- LLM은 최신 정보나 학습되지 않은 데이터를 모름. 따라서 모델에게 정보를 직접 제공해야 할 때가 많음. LLM은 대화의 흐름을 기억하므로, 이전에 제공한 정보를 활용해 답변이 가능함.

    Ex. 정보 제공하기
        - User : 정석이는 26살이고 올해 대학교 졸업해서 개발자 쪽으로 취업 준비를 하고 있어. 여자친구랑 헤어져서 좀 힘들다던데 정석이에게 응원하는 글 좀 써줘.
        - Assistant : 정석이에게,
        안녕하세요, 정석이! 먼저, 대학교 졸업을 진심으로 축하드려요. 새로운 시작을 앞두고 있는 지금, 그동안 쏟은 노력과 열정이 결실을 맺을 시간이 온 것 같아요. 개발자라는 멋진 꿈을 향해 나아가고 있는 모습, 정말 자랑스럽습니다.

        헤어진 여자친구 때문에 힘든 시간을 보내고 있다는 소식을 들었어요. 힘든 상황이지만, 이러한 시간 역시 정석이를 더 단단하게 만들어 줄 것이라 믿어요. 때로는 아픔이 성장을 위한 밑거름이 되기도 하니까요.

        힘들 때는 잠시 쉬어가도 괜찮아요. 스스로에게 너그럽고, 주변의 친구들이나 가족들과 이야기를 나누면서 마음의 짐을 조금 덜어보세요. 당신의 가치는 어떤 상황에서도 변하지 않는다는 것을 잊지 않았으면 좋겠어요.

        정석이의 앞날에 좋은 일들이 가득하기를 진심으로 응원합니다. 당신의 열정과 노력이 반드시 멋진 결과로 이어지길 바라며, 언제나 행복과 웃음이 함께하길 바랍니다. 힘내세요!

        언제나 응원합니다.

- 특정 인물에 대한 정보를 제공하여, 개인적인 응원의 글을 작성 가능.

### 제약 조건 설정

- 제약 조건 설정 시, 더 명확한 결과 얻을 수 있음. 답변의 길이나 특정한 정보만 포함하는 것 등 다양하게 적용 가능.

    Ex. 제약 조건 없이 요청  
        - User : 배우 박은빈에 대해서 설명해줘  

        - Assistant : 박은빈은 대한민국의 배우로, 어린 시절부터 꾸준히 활동해온 실력파 배우 중 한 명입니다. 1992년 9월 4일에 태어난 그녀는 1996년에 아동복 모델로 연예계에 입문하여, 이후 다양한 드라마와 영화에서 인상적인 연기를 선보였습니다.  

        박은빈은 그동안 여러 작품에서 다채로운 캐릭터를 소화하며 연기력을 인정받았습니다. 대표적인 작품으로는 드라마 '청춘시대', '스토브리그', '브람스를 좋아하세요?' 등이 있습니다. 특히 2022년 드라마 '이상한 변호사 우영우'에서 독특한 캐릭터를 연기하며 큰 호평을 받았고, 대중적인 인기를 얻었습니다.  

        그녀는 섬세하고 깊이 있는 연기를 통해 많은 팬들에게 사랑받고 있으며, 앞으로도 다양한 작품에서 활약할 가능성이 높은 배우입니다. 박은빈의 차분하고 정감 있는 이미지와 뛰어난 연기력은 그녀의 큰 매력이자 강점입니다.  

- 정보가 많아 길어서 요점 파악이 힘듦.

    Ex. 제약 조건 추가  
        - User : 배우 박은빈의 주요 정보 3가지만 말해줘  

        - Assistant : 물론입니다. 배우 박은빈의 주요 정보를 세 가지로 요약해드리겠습니다.  

        1. **연기 경력**: 박은빈은 1996년 아역 배우로 연예계에 데뷔하여 어린 시절부터 다양한 드라마와 영화에 출연하며 탄탄한 연기 경력을 쌓아왔습니다.  

        2. **대표 작품**: 그녀는 '청춘시대', '스토브리그', '브람스를 좋아하세요?', 그리고 '이상한 변호사 우영우' 등에서 주연을 맡으며 많은 사랑을 받았습니다.  

        3. **다재다능한 배우**: 박은빈은 다양한 장르와 캐릭터를 소화하는 능력을 가지고 있으며, 특히 섬세하고 진정성 있는 연기로 많은 팬들의 지지를 받고 있습니다.  

- 원하는 정보만 깔끔히 제공 받기가 가능.

### 작업 분할

- 복잡한 작업을 한번에 요청하면, LLM이 잘못된 답변을 줄 수 있음. 작업을 여러 단계로 나누어 요청하는 것이 더 효율적. 특히 코드 작성 및 긴 텍스트 요약에서는 작업 분할이 유용.

    Ex. 긴 텍스트 요약  
        - User : '열혈사제'라는 드라마를 짧게 세 단락으로 요약하고 싶어.  
        첫 번째 단락은  이영준 신부가 죽고 김해일 신부가 구대영 형사와 공조하는 과정, 두 번째 단락은 박경선 검사의 교화와 구대영 형사의 진실, 마지막 단락은 이영준 신부의 죽음의 진실을 밝히고 모든 사건을 처리한 과정으로 구성해줘  

        - Assistant : 드라마 '열혈사제'는 정의를 위해 돌진하는 신부와 형사의 이야기를 그린 작품입니다. 첫 번째 단락에서는, 이영준 신부가 의문의 죽음을 맞이하게 되면서 이야기가 시작됩니다. 그의 죽음에 의문을 품은 김해일 신부는 복수를 다짐하고, 우연한 사건으로 만난 구대영 형사와 협력하게 됩니다. 두 사람은 서로 다른 성격과 출신 배경으로 처음에는 충돌하지만, 점차 협력하며 사건의 진실에 접근합니다.  

        두 번째 단락에서는 박경선 검사와 구대영 형사의 변화가 중심이 됩니다. 처음에는 개인의 이익과 현실적인 안주를 좇던 박경선 검사는 점차 김해일 신부와의 협력 속에서 정의감에 눈을 뜨게 됩니다. 동시에, 구대영 형사는 사건의 진실에 가까워지며 자신의 의무를 다하려는 결심을 확고히 합니다. 이들은 함께 부패한 사회 시스템과 마주하며 객체적인 시각에서 공조를 이루어 나갑니다.  

        마지막 단락에서는 이영준 신부의 죽음 뒤에 숨겨진 진실이 드러나고, 김해일 신부와 구대영 형사, 박경선 검사는 끝까지 포기하지 않고 싸우며 진실을 밝혀냅니다. 여러 난관과 적대 세력의 방해에도 불구하고, 이들은 이영준 신부의 억울한 죽음을 둘러싼 모든 사건을 해결합니다. 정의를 위해 끝까지 최선을 다하는 이들의 노력으로 부패한 인물들이 처벌받고, 작은 정의가 실현되는 장면이 그려집니다. 드라마는 이들의 치열한 싸움을 통해 정의의 중요성을 되새기며 마무리됩니다.  

## Shot 계열 프롬프팅

- shot은 AI에게 전달하는 예제를 의미함.

### Zero-Shot 프롬프팅

- 아무런 예제를 주지 않고 지침만 전달하는 방식. AI에게 추상적인 요청을 하면, 기대한 답변을 받기 어려운 경우가 허다함.

    Ex.  
        - System: 너는 전달된 구구단에 대한 농담을 해야해.  
        - User: 6 * 3  
        - Assistant: 왜 6은 3을 곱하면 항상 놀라는 표정을 짓는 걸까요?  
        왜냐하면 답이 18이라고 귓속말로 말해주니까요!  

### One-Shot 프롬프팅

- Shot을 즉, 예제를 하나 전달해주는 방식.

    Ex.  
        - System: 너는 구구단 농담을 하는 인공지능이야. 이건 구구단 농담의 예시야. "6*3은 육삼빌딩"  
        - User: 2*4  
        - Assistant: 2*4 : 이사오세요  

- 의도에 맞는 답변이 도출.

### Few-Shot 프롬프팅

- 여러 개의 예시를 주어, 모델이 더 잘 학습되도록.
- 많은 예제로 유도하는 능력이 향상됨.

    Ex.  
        - System: 너는 예를 참고해서 전달된 구구단에 대한 농담을 해야해. 과정은 말하지 말고 농담만 말해.  
        '입력 : 6*4, 출력: 육사생도', '입력: 2*8, 출력: 이팔 청춘', '입력: 5*2, 출력: 오이팩'  
        - User: 2*4  
        - Assistant: 이사갈 시간  
        - User: 3*8  
        - Assistant: 삼팔광땡  
        - User: 2*6  
        - Assistant: 이육사  

- Few-Shot 프롬프팅 도중에, 입력과 출력만 제공하는 것보다 과정도 같이 제공하면 모델의 추론 능력도 향상되어 효과적.

    Ex.  
    '입력 : 6*4, 출력: 육사생도, 과정: 6*4는 '육곱하기사'야. 여기서 '곱하기'를 빼면 '육사'가 되지? '육사'로 시작하는 단어를 찾은 거야.'  

- 실습 예시 : 영화 맞추기 자음 게임  
![few-shot](./picture/few-shot%20prompting.JPG)  

## Act As(Persona) 프롬프팅 기법 배우기

- AI에게 성격이나 역할을 부여하는 프롬프팅 기법.

### 페르소나(Persona)

- LLM에게 성격, 관점, 또는 역할을 부여하는 것.
- Act As는 '너는 ~처럼 행동해'라는 식으로 역할을 주는 프롬프트의 한 형태.
- 예로 '너는 변호사야'라고 한다면, 법적인 조언을 하도록 모델을 유도 가능.
- 페르소나 지정은 객관적 정보를 얻기보단 특정 관점이나 전문적 답변을 원할 때 유용.
- 또한, 브랜드의 챗봇처럼 회사 정체성이 필요한 경우도 많이 사용됨.

    Ex.  
        - System : 너는 변호사야.  

### Act As

- 역할 부여 프롬프트. 모델에게 특정 직업, 역할을 부여해 그 직업이나 성격에 맞는 답을 얻을 수 있음.

    Ex.  
        - System : 너는 변호사야.  
        - System : 너는 건축가야.  

### 페르소나 설정의 구체화

- 페르소나 지정 시 더 구체적으로 지침을 주면 역할의 특성을 더 잘 반영할 수 있음.

    Ex.  
        - System : 너는 변호사야. 변호사의 관점에서 법적으로 전문적인 답변을 작성해.  
        - System: 너는 개그맨이야. 개그맨처럼 재미있게 답변해.  

### 페르소나 창조하기

- 완전히 새로운 페르소나를 만들 수도 있음. 예로, "조윤이"라는 가상의 인물에게 성격과 취업을 설정한 후, 그 인물의 관점에서 답변하도록 할 수 있음.

    Ex.  
        - System: 너는 조윤이야. 조윤이의 관점에서 답변을 작성해.  
        이름: 조윤이  
        성격: 외향적이고 적인 성격. 사람들과 어울리는 걸 좋아하며, 도전을 추구하는 성격.  
        직업: 사회복지사. 봉사 및 행사 프로젝트를 만들어 지역사회에 기여.  
        특징: 체계적이고 꼼꼼하며, 사회 봉사와 아이들에 관심이 많음.  

### 도구의 페르소나 부여하기

- 사람에게만 적용되는 것이 아님. 프로그램이나 도구에도 부여 가능. 예로, 파이썬 인터프리터 처럼 행동하게 할 수가 있음.

    Ex.  
        - System : 너는 파이썬 인터프리터야.  
        - User : A = 10 B = 20 print(A + B)  
        - Assistant: The code initializes two variables, A and B, with values 10 and 20, respectively. When you run this code in Python, it will output 30.  

## 논리적인 추론 강화하기

- LLM은 기본적으로 확률에 기반해 작동. 논리적 추론 능력이 상대적으로 부족할 수 있음. 따라서 논리적인 답변을 기대할 때는 구체적 지침을 주는 것이 매우 중요.

### 논리적 추론의 한계