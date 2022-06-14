//즉시 호출 함수를 만듭니다. 이렇게 만들어 놓으면 함수가 자동으로 호출 됩니다.
// (function () {})(); 이 함수랑 밑에 있는 즉시 호출 함수랑 동일한 코드입니다.
// 전역변수 사용을 피하려고 밑 코드를 사용합니다.
(() => {
    let yOffset = 0; //window.pageYOffset 대신 쓸 함수
    let prevScrollHeight = 0; //현재 스크롤 위치(yOffset)보다 이전에 위치한 스크롤 섹션들의 스크롤 높이값의 합
    let currentScene = 0; // 현재 활성화된(눈 앞에 보고있는) 씬(scroll-section)

    const sceneInfo = [
        {
            //scrollSection 0
            type: 'sticky',
            heightNum: 5,
            scrollHeight: 0,
            objs: {
                container: document.querySelector('#scroll-section-0')
            }
        },
        {
            //scrollSection 1
            type: 'nomal',
            heightNum: 5,
            scrollHeight: 0, 
            objs: {
                container: document.querySelector('#scroll-section-1')
            }
        },
        {
            //scrollSection 2
            type: 'sticky',
            heightNum: 5,
            scrollHeight: 0, 
            objs: {
                container: document.querySelector('#scroll-section-2')
            }
        },
        {
            //scrollSection 3
            type: 'sticky',
            heightNum: 5,
            scrollHeight: 0,
            objs: {
                container: document.querySelector('#scroll-section-3')
            } 
        }
    ];

    function setLayout() {
        //각 스크롤 섹션의 높이 세팅
        for (let i = 0; i<sceneInfo.length; i++) {
            sceneInfo[i].scrollHeight = sceneInfo[i].heightNum *window.innerHeight;
            sceneInfo[i].objs.container.style.height=`${sceneInfo[i].scrollHeight}px`;
        }
    }


    function scrollLoop() {
        prevScrollHeight = 0;
        for (let i = 0; i < currentScene; i++){
            prevScrollHeight += sceneInfo[i].scrollHeight;
        }
        if (yOffset > prevScrollHeight + sceneInfo[currentScene].scrollHeight) {
            currentScene++;
        }
        if (yOffset < prevScrollHeight) {
            if (currentScene === 0) return; //브라우저 바운스 효과로 인해 마이너스가 되는 것을 방지(아마 모바일)
            currnetScene--;
        }
        console.log(currentScene);
    }


    window.addEventListener('resize', setLayout);
    window.addEventListener('scroll', () => {
        yOffset = window.pageYOffset;
        scrollLoop();
    });

    setLayout();

})();