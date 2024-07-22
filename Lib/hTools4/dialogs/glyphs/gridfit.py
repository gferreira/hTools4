import ezui


class RoundToGridDialog(ezui.WindowController):

    title   = 'gridfit'
    width   = 123
    margins = 10

    def build(self):
        content = """
        grid
        [__](±)         @grid

        [X] bPoints     @options
        [X] points
        [X] margins
        [X] width
        [X] anchors
        [X] components

        (apply)         @applyButton

        [ ] preview     @preview
        [ ] show grid   @showGrid
        """
        descriptionData = dict(
            content=dict(
                sizeStyle="small"
            ),
            applyButton=dict(
                width="fill",
            ),
        )
        self.w = ezui.EZPanel(
            title=self.title,
            content=content,
            descriptionData=descriptionData,
            controller=self,
            margins=self.margins,
            size=(self.width, 'auto'),
        )

    def started(self):
        self.w.getNSWindow().setTitlebarAppearsTransparent_(True)
        self.w.open()


if __name__ == "__main__":

    RoundToGridDialog()
